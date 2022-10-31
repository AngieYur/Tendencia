from django.views.generic import DetailView
from django.views.generic.list import ListView

# create your views here
from .models import Inventario


class ListaInventario(ListView):
    model = Inventario
    context_object_name = "inventarios"


class DetalleInventario(DetailView):
   model = Inventario
   template_name = "concesionario/detalle_inventario.html"
   context_object_name = "inventario"