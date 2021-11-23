from rest_framework.routers import DefaultRouter
from nights_noroeste.api.views import NigthsNoroesteApiViewSet

router_nights_noroeste = DefaultRouter()
router_nights_noroeste.register(prefix='night_noroeste', basename='night_noroeste', viewset=NigthsNoroesteApiViewSet )