from django.shortcuts import render
from . import models

# home page
def home(request):
    banners = models.Banners.objects.all()
    return render(request,'home.html',{'banners':banners})

def pricing(request):
    return render(request,'pricing.html')

