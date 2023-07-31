from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'name':'lahari','age':22}
    return render (request,'data_render.html',context=d)
def condition(request):
    d={'a':10,'b':20}
    return render(request,'condition.html',context=d)
def condition1(request):
    d={'a':100,'b':200}
    return render(request,'condition1.html',context=d)
def condition2(request):
    d={'a':300,'b':500}
    return render(request,'condition2.html',context=d)
def condition3(request):
    d={'a':1000,'b':2000}
    return render(request,'condition3.html',context=d)