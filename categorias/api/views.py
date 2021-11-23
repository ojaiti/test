from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from categorias.models import Category
from categorias.api.serializers import CategorySerializer
from categorias.api.permissions import IsAdminOrReadOnly


class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly] # permisos para ver los endpoints
    serializer_class = CategorySerializer # genera el crud completo en los endpoints
    queryset = Category.objects.all() #Devuelve todos los datos
    #queryset = Category.objects.filter(published =True) #Filtos de Django
    lookup_field = 'slug' #Esto reemplsaza el id por el name de la categoria
    filter_backends = [DjangoFilterBackend] #Filtros de Django
    filterset_fields = ['published', 'title'] #Campos para poder filtrar en los endpoints