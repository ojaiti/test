from rest_framework import serializers
from comments.models import Comment
from users.api.serializer import UserSerializer
from posts.api.serializers import PostSerializer
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer() #Para tener el nombre y no el id
    post = PostSerializer()
    class Meta:
        model = Comment
        fields = ['content', 'created_at', 'user', 'post']
