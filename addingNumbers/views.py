from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
def input(request):
    return render(request, 'input.html')
def add(request):
    x = request.GET.get("t1")
    y = request.GET.get("t2")
    i = int(x)
    j = int(y)
    z = i+j
    cont_dict = {'sum':z}
    return render(request,"result.html", context=cont_dict)
