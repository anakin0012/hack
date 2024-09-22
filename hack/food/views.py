from django.shortcuts import render

def map_C_view(request):
    return render(request, 'map_C.html')

def map_E_view(request):
    return render(request, 'map_E.html')

def map_J_view(request):
    return render(request, 'map_J.html')
