from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html')


def clientes(request):
    return render(request, 'pages/clientes.html')