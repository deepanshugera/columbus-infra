from django.shortcuts import render
from .forms import CodeForm
# Create your views here.
from django.http import HttpResponse

def hello(request):

   result="hii"
   return render(request,"interface/home.html",{"res":result})

def upload_file(request):
   #file upload
   user_code=""
   return render(request,"interface/command.html",{"user_code":user_code})

def exec_command(request):

   result="my result comes here"
   user_code=""
   if request.method == 'POST':
      user_code=request.POST.get('code')
      result="result_goes_here"
   return render(request,"interface/command.html",{"user_code":user_code,"result":result})
