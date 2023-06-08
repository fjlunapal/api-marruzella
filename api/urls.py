from django.urls import path, re_path

from django_api import settings
from .views import *
from django.conf.urls.static import static

app_name = 'api'

urlpatterns = [
    path('producto', Producto_APIView.as_view()),
    path('productoCarrito', ProductoCarrito_APIView.as_view()),
    path('pedido', Pedido_APIView.as_view()),
    path('pedido/<int:pk>/', Pedido_APIView.as_view()),  # Modificación aquí
    re_path('^productoCarrito/(?P<pedidoId>.+)/$', ProductoCarritoList.as_view()),
    path('user/login', UserViewSet.as_view({'post': 'login'})),
    path('user/register', UserViewSet.as_view({'post': 'register'})),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)