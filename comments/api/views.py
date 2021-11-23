from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from comments.models import Comment
from comments.api.serializers import CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from comments.api.permissions import IsOwnerOrReadAndCreateOnly

class CommentApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering = ['-created_at'] #se utiliza un - si quiered ordenarlos ascendente o descentent ejemplo descendente[-created_at]
    filterset_fields = ['post']
