from django.urls import path

from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.productos_all, name='productos_all'),
    path('libro/<slug:slug>/', views.producto_detail, name='producto_detail'),
    path('search/<slug:categoria_slug>/', views.category_list, name='category_list'),
    path('acerca', views.acerca, name='acerca'),
    





    
]
