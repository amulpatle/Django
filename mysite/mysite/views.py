from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("hey my name is amul")