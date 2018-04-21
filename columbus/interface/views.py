from django.shortcuts import render
from .forms import CodeForm
# Create your views here.
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def hello(request):

   result="hii"
   return render(request,"interface/home.html",{"res":result})

def upload_file(request):
   #file upload
   user_code = ""
   if request.method == 'POST' and request.FILES['csv_file']:
      csv_file = request.FILES['csv_file']
      fs = FileSystemStorage()
      filename = fs.save(csv_file.name, csv_file)
      request.session['csv_file'] = filename
      uploaded_file_url = fs.url(filename)
      return render(request, "interface/command.html", {"user_code": user_code,'success': uploaded_file_url+" uploaded successfully"})
   return render(request,"interface/home.html",{"error":"Unable to upload file"})

def exec_command(request):
   #last csv file uploaded by the user
   csv_file=request.session['csv_file']
   #variable to store the result
   result=""
   #variable to hold the user code
   user_code=""
   if request.method == 'POST':
      user_code=request.POST.get('code')
      result="result_goes_here"
   return render(request,"interface/command.html",{"user_code":user_code,"result":result})
