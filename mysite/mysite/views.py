from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    
    return HttpResponse("hey my name is amul")

def homePage(request):
    data = {
        'title':'hey Page',
        'para':'this is new (^ ^)',
        'clist':['PHP','JAVA','Django'],
        'numbers' : [10,20,30,40,50],
        'student_details':[
            {'name':'Amul','Phone':7222999446},
            {'name':"Atul",'Phone':8839104827}
        ]
    }
    return render(request,"index.html",data)

