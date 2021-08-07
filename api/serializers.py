from rest_framework import serializers
from .models import PostStatistics


class PostSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    post_id = serializers.IntegerField()
    likes_count = serializers.IntegerField()


class PostStatisticsSerializer(serializers.ModelSerializer):
    post_id = serializers.IntegerField(source='post.id')
    class Meta:
        model = PostStatistics
        fields = ("user_id", "post_id", "likes_count")
