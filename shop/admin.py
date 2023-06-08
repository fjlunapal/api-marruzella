from django.contrib import admin
from .models import Producto, ProductoCarrito, Pedido

admin.site.register(Producto)
admin.site.register(ProductoCarrito)
admin.site.register(Pedido)

