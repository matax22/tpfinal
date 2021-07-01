from decimal import Decimal
from django.conf import settings
from tienda.models import Producto
from django.http import JsonResponse


class Basket():
    """
    Clase basica de carrito
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, producto, qty):

        producto_id = str(producto.id)

        if producto_id in self.basket:
            self.basket[producto_id]['qty'] = qty
        else:
            self.basket[producto_id] = {'precio': str(producto.precio), 'qty': qty}

        self.save()  

    def __iter__(self):

        producto_ids = self.basket.keys()
        productos  = Producto.productos.filter(id__in=producto_ids)
        basket = self.basket.copy()
       
        for producto in productos:
            basket[str(producto.id)]['producto'] = producto   

        for item in basket.values():
            item['precio'] = Decimal(item['precio'])
            item['total_precio'] = item ['precio'] * item['qty']
            yield item
    


    def __len__(self):
        """
        Juntar los datos del carro, y contar la cantidad de items
        """
        return sum(item['qty'] for item in self.basket.values())

    def update(self, producto, qty):
        """
        Update values in session data
        """
        producto_id = str(producto)
        if producto_id in self.basket:
            self.basket[producto_id]['qty'] = qty
        self.save()

    def precio_total(self):
        return sum(Decimal(item['precio']) * item['qty'] for item in self.basket.values())

    def delete(self, producto):
        '''
        borrar items de nuestra sesion
        '''

        producto_id = str(producto)
        
        if producto_id in self.basket:
            del self.basket[producto_id]
            print(producto_id)
            self.save()


    def save(self):
        self.session.modified = True







