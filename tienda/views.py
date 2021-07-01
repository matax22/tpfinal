from .models import Categoria, Producto
from django.shortcuts import get_object_or_404, render
# Create your views here.


def productos_all(request):
    productos= Producto.objects.filter(activo=True)
    return render(request, 'tienda/home.html', {'productos': productos})


def producto_detail(request, slug):
    producto = get_object_or_404(Producto, slug=slug, stock=True)
    return render(request, 'tienda/productos/single.html', {'producto' : producto})

def category_list(request, categoria_slug=None):
    categoria = get_object_or_404(Categoria, slug=categoria_slug)
    productos = Producto.objects.filter(categoria=categoria)
    return render(request, 'tienda/productos/categoria.html', {'categoria': categoria, 'productos': productos})

def acerca(request):
    return render(request, 'tienda/acerca.html')
