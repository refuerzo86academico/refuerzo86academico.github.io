from django.shortcuts import render

# Create your views here.
#arreglar los links, no se abren bien.

def home(request):
    return render(request, "refuerzo86/home.html")

def about(request):
    return render(request, "refuerzo86/about.html")

def productos(request):
    return render(request, "refuerzo86/productos.html")

def precio(request):
    return render(request, "refuerzo86/precio.html")

def nosotros(request):
    return render(request, "refuerzo86/nosotros.html")

def contacto(request):
    return render(request, "refuerzo86/contacto.html")
