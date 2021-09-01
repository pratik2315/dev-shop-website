from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')
    #return HttpResponse('hello world')

def aboutUs(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contactUS(request):
    return render(request, 'contact.html')