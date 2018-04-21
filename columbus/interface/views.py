from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):

   result="hi"
   return render(request,"interface/home.html",{"res":result})
