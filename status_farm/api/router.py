from rest_framework.routers import DefaultRouter
from status_farm.api.views import StatusFarmApiViewSet

router_status_farm = DefaultRouter()
router_status_farm.register(prefix='status_farm', basename='status_farm', viewset = StatusFarmApiViewSet)