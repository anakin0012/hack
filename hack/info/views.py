from django.shortcuts import render

def Emergency_view(request):
    return render(request, 'emergency-en.html')

def Hospital_view(request):
    return render(request, 'hospital-en.html')

def Hospital_cn_view(request):
    return render(request, 'hospital-cn.html')

def Hospital_jp_view(request):
    return render(request, 'hospital-jp.html')

def Mbank_view(request):
    return render(request, 'Mbank-en.html')

def Mmobile_view(request):
    return render(request, 'Mmobile-en.html')

def Pt_view(request):
    return render(request, 'Pt-en.html')

def Waste_view(request):
    return render(request, 'Waste_separation-en.html')
