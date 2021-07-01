from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(activo=True)


class Categoria(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)


    class meta:
        verbose_name_plural = 'Categorias'

    def get_absolute_url(self):
        return reverse('tienda:category_list', args=[self.slug])


    def __str__(self):
        return self.name



class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='producto', on_delete=models.CASCADE)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='creador_producto' )
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255, default='admin')
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='images/', default='images/default.jpg')
    slug = models.SlugField(max_length=255)
    stock = models.BooleanField(default=True)
    precio = models.DecimalField(max_digits=4, decimal_places=2)
    activo = models.BooleanField(default=True)
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateField(auto_now=True)
    productos = ProductManager()
    objects = models.Manager()

    

    

    class Meta:
        verbose_name_plural = 'Productos'
        ordering = ('-creado',)

    def get_absolute_url(self):
        return reverse('tienda:producto_detail', args=[self.slug] )
        


    def __str__(self):
        return self.titulo


        




