from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def collection(request):
    return render(request, 'collection.html')

def about_us(request):
    return render(request, 'about_us.html')