from django.shortcuts import render

# Create your views here.
def radha(request):
    d={"name":"ganesh","age":"23"}
    return render (request,'krishna.html',context=d)
def gani (request):
    g={"num":"200731058"}
    return render (request,'gani.html',context=g)    