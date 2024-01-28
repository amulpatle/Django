from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return HttpResponse("hey my name is amul")

def homePage(request,):
    data = {
        'title':'Home Page',
    }
    return render(request,"index.html")

