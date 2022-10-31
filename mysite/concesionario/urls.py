from django.urls import path

#from concesionario import views

from .views import ListaInventario, DetalleInventario

urlpatterns = [
    path('', ListaInventario.as_view(), name='inventario'),
    path('<int:pk>', DetalleInventario.as_view(), name='detalleinventario')


]
