from django.shortcuts import render

def Emergency_view(request):
    return render(request, 'emergency-en.html')

def Mbank_view(request):
    return render(request, 'Mbank-en.html')

def Mmobile_view(request):
    return render(request, 'Mmobile-en.html')

def Pt_view(request):
    return render(request, 'Pt-en.html')

def Waste_view(request):
    return render(request, 'Waste_separation-en.html')
