from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import DatabaseError, transaction
from .models import Post, PostStatistics
from .serializers import PostSerializer, PostStatisticsSerializer


class PostCreateView(APIView):
    def post(self, request):
        Post.objects.all().delete()
        PostStatistics.objects.all().delete()
        serializer = PostSerializer(data=request.data, many=True)
        if serializer.is_valid():
            for item in request.data:
                try:
                    with transaction.atomic():
                        post = Post.objects.filter(post_id=item['post_id']).first()
                        if post is None:
                            post = Post(post_id=item['post_id'], user_id=item['user_id'])
                            post.save()
                        post_statistics = PostStatistics(post=post, likes_count=item['likes_count'],
                                                         user_id=item['user_id'])
                        post_statistics.save()

                except DatabaseError:
                    Response({"failure": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"failure": "Bad request"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"success": "{} posts saved successfully".format(len(request.data))},
                        status=status.HTTP_201_CREATED)

