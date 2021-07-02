from typing import Mapping
from django.db import router
from django.urls import path
from django.urls.conf import include
from core.views import home, about, menu, contact, apirest, registro_usuario, staffUsers, listado_productos, listado_tipos, nuevo_producto, nuevo_tipo, modificar_producto, eliminar_producto, modificar_tipo, eliminar_tipo, listado_usuarios, eliminar_usuario, modificar_usuario
from AppProductos.views import ProductViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos', ProductViewSet)

urlpatterns = [
    path('', home, name="home"),
    path('sobre-nosotros/', about, name='about'),
    path('nuestro-menu/', menu, name='menu'),
    path('contacto/', contact, name='contact'),
    path('api-rest/', apirest, name='apirest'),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('staff-sushi/', staffUsers, name='staffUsers'),
    path('staff-sushi/listado-productos/', listado_productos, name='listado_productos'),
    path('staff-sushi/listado-tipos/', listado_tipos, name='listado_tipos'),
    path('staff-sushi/nuevo-producto/', nuevo_producto, name='nuevo_producto'),
    path('staff-sushi/nuevo-tipo/', nuevo_tipo, name='nuevo_tipo'),
    path('staff-sushi/modificar-producto/<id>/', modificar_producto, name='modificar_producto'),
    path('staff-sushi/eliminar-producto/<id>/', eliminar_producto, name='eliminar_producto'),
    path('staff-sushi/modificar-tipo/<id>/', modificar_tipo, name='modificar_tipo'),
    path('staff-sushi/eliminar-tipo/<id>/', eliminar_tipo, name='eliminar_tipo'),
    path('staff-sushi/listado-usuarios/', listado_usuarios, name='listado_usuarios'),
    path('staff-sushi/eliminar-usuario/<id>/', eliminar_usuario, name='eliminar_usuario'),
    path('staff-sushi/modificar-usuario/<id>/', modificar_usuario, name='modificar_usuario'),
    path('api/', include(router.urls)),
]