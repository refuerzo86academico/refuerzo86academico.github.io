from django.urls import path
from . import views

#agrego la funcion de views de quehaceres(app) que debo importar antes

urlpatterns = [
    path("",views.home, name="home"),
    path("about.html/", views.about, name="about"),
    path("productos.html/", views.productos, name="productos"),
    path("precio.html/", views.precio, name="precio"),
    path("nosotros.html/", views.nosotros, name="nosotros"),
    path("contacto.html/", views.contacto, name="contacto"),
    

]
