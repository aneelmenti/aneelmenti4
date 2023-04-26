from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def getinput(request):
    return render(request,'getinput.html')
def postinput(request):
    return render(request,'postinput.html')
def add(request):
    if request.method=='GET':
        a=request.GET["t1"]
        b=request.GET["t2"]
        i=int(a)
        j=int(b)
        k=i+j
        res=HttpResponse("The sum is: "+str(k))
        return res
    elif request.method=='POST':
        a=request.POST["t1"]
        b=request.POST["t2"]
        i=int(a)
        j=int(b)
        k=i+j
        res=HttpResponse("The sum is: "+str(k))
        return res
