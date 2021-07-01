
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from tienda.models import Producto
from .basket import Basket


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'tienda/basket/summary.html', {'basket': basket})



def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        producto_id =int(request.POST.get('productoid'))
        producto_qty =int(request.POST.get('productoqty'))
        producto = get_object_or_404(Producto, id=producto_id)
        basket.add(producto=producto, qty=producto_qty)    
        
          
        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        producto_id =int(request.POST.get('productoid'))
        basket.delete(producto=producto_id)

        basketqty = basket.__len__()
        baskettotal = basket.precio_total()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response



def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        producto_id = int(request.POST.get('productoid'))
        producto_qty = int(request.POST.get('productoqty'))
        basket.update(producto=producto_id, qty=producto_qty)

        basketqty = basket.__len__()
        baskettotal = basket.precio_total()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response
