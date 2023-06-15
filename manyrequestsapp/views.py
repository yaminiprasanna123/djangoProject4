from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')

def getinput(request):
    return render(request,'getinput.html')

def postinput(request):
    return render(request,'postinput.html')
def add(request):
    if request.method=="GET":
        p=int(request.GET["t1"])
        q=int(request.GET["t2"])
        r=p+q
        return HttpResponse("The sum is: "+str(r))
    else:
        x=int(request.POST["t1"])
        y=int(request.POST["t2"])
        z=x+y
        return HttpResponse("The sum is: "+str(z))