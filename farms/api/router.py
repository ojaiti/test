from rest_framework.routers import DefaultRouter
from farms.api.views import FarmsApiViewSet

router_farms = DefaultRouter()
router_farms.register(prefix='farms', basename='farms', viewset = FarmsApiViewSet)