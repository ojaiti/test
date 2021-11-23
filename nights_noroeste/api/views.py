from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from nights_noroeste.models import NightsNoroeste
from nights_noroeste.api.serializers import NightsNoroesteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from nights_noroeste.api.permissions import IsAdminOrReadOnly

class NigthsNoroesteApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = NightsNoroesteSerializer
    queryset = NightsNoroeste.objects.filter(farm_origen=2)
    queryset = NightsNoroeste.objects.filter(farm_origen=2).select_related('farm_origen')
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering = ['-farm_origen']
    

