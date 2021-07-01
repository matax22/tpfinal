from django.contrib import admin

# Register your models here.

from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} 


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
       list_display = ['titulo', 'autor', 'slug', 'precio', 'creado', 'actualizado',
                      'stock',]
       list_filter = ['stock', 'activo']      
       list_editable = ['precio', 'stock',]
       prepopulated_fields = {'slug': ('titulo',)}          