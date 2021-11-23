from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from farms.models import Farm
from farms.api.serializers import FarmsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from farms.api.permissions import IsAdminOrReadOnly

class FarmsApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = FarmsSerializer
    queryset = Farm.objects.all()
    #filter_backends = [DjangoFilterBackend, OrderingFilter]
    #ordering = ['-farm_origen']