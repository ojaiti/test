from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from status_farm.models import StatusFarm
from status_farm.api.serializers import StatusFarmSerializer
from django_filters.rest_framework import DjangoFilterBackend
from farms.api.permissions import IsAdminOrReadOnly

class StatusFarmApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = StatusFarmSerializer
    queryset = StatusFarm.objects.all()
    #filter_backends = [DjangoFilterBackend, OrderingFilter]
    #ordering = ['-farm_origen']