
from django.contrib import admin
from django.urls import path, include
# from aplicativo.api.viewsets import views
from tutorial2 import urls 
from django.conf import settings
from rest_framework import routers
from django.contrib import admin


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(views.urls))
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from aplicativo.api.viewsets import CarrosViewSet

# Criar um roteador padrão
router = DefaultRouter()

# Registrar o viewset do Carro com o roteador
router.register(r'carros', CarrosViewSet, basename="Carro")

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluir as rotas do roteador
    path('', include(router.urls)),
]
