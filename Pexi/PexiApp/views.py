from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import *

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Login_model

class Login(View):
    def get(self, request):
        return render(request, 'admin/pexi_admin_login.html')

    def post(self, request):
        username = request.POST["username"]
        password = request.POST['password']

        obj=Login_model.objects.get(username=username,password=password)
        if obj.type == 'admin':
               return HttpResponse('''<script>alert('login succesfully');window.location='/home_page/'</script>''')
        
class cmpmenu(View):
    def get(self,request):
        return render(request, 'admin/usercomplaints.html')
class driver_details(View):
    def get(self, request):
        return render(request, 'admin/driver_details.html')
class drivercmp(View):
    def get(self, request):
        c=Complanits_model.objects.filter(LOGINID__type='driver')
        print(c)
        return render(request, 'admin/drivercmp.html',{'c':c})
class drivers(View):
    def get(self, request):
        c=Driver_model.objects.all()
        print(c)
        return render(request, 'admin/drivers.html',{'c':c})
    
# class get driverdetails(View):
#     def get(self,request,id):
#         c=Driver_model.objects.get(id=id)
#         return render(request, 'admin/driver_details.html',{'c':c})
class home_page(View): 
    def get(self, request):
        return render(request, 'admin/home_page.html')
class ucmp2(View):
    def get(self, request):
        return render(request, 'admin/ucmp2.html')
class usercomplaints(View):
    def get(self, request):
        c=Complanits_model.objects.filter(LOGINID__type='user')
        print(c)
        return render(request, 'admin/usercomplaints.html',{'c':c})
class userdetails(View):
    def get(self, request):
        return render(request, 'admin/userdetails.html')
    
    
class users(View):
    def get(self, request):
        c=User_model.objects.all()
        print(c)
        return render(request, 'admin/users.html',{'c':c})
    
class complaintdisplay(View):
    def get(self, request):
        return render(request, 'admin/cmpmenu.html')
class AllFeedback(View):
    def get(self,request):
        return render(request, 'admin/AllFeedback.html')
class driverfeedback(View):
    def get(self,request):
        c=Feedback_model.objects.filter(type='driverfeedback')
        print(c)
        return render(request, 'admin/driverfeedback.html',{'c':c})
class Userfeedback(View):
    def get(self,request):
        c=Feedback_model.objects.filter(type="userfeedback")
        return render(request, 'admin/Userfeedback.html',{'c':c})
class dcmp2(View):
    def get(self,request):
        return render(request, 'admin/dcmp2.html')