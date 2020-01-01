from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    #return HttpResponse()
    return render(request, 'calc.html')

def images(request):
    #return HttpResponse("This will return images in few minutes")
    img_tuple = ['1.jpg','2.jpg','3.jpg']
    return render(request,'images.html',{'imgs':img_tuple})