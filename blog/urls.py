"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from posts.api.router import router_posts
from categorias.api.router import router_categories
from comments.api.router import router_comment
from farms.api.router import router_farms
from nights_noroeste.api.router import router_nights_noroeste
#Modificacion del titulo del panel de administrador
from django.contrib import admin
admin.site.site_header = 'Administración de visitas a las granjas'

#schema para la documentación
schema_view = get_schema_view(
   openapi.Info(
      title="Monitor Granjas Ojai",
      default_version='v1',
      description="Documentación de la api de granjas ojai",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="javier.felix@grupoojai.mx"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
    path('api/', include('users.api.router')), #APIVIEW
    path('api/', include(router_categories.urls)),#MODELVIEWSET -  
    path('api/', include(router_posts.urls)),
    path('api/', include(router_comment.urls)),
    path('api/', include(router_nights_noroeste.urls)),
    path('api/', include(router_farms.urls))
]
