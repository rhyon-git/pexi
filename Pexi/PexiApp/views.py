from django.shortcuts import render
from django.views import View

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, 'admin/pexi_admin_login.html')
class cmpmenu(View):
    def get(self,request):
        return render(request,'admin/cmpmenu.html')
class driver_details(View):
    def get(self, request):
        return render(request, 'admin/driver_details.html')
class drivercmp(View):
    def get(self, request):
        return render(request, 'admin/drivercmp.html')
class drivers(View):
    def get(self, request):
        return render(request, 'admin/drivers.html')
class home_page(View): 
    def get(self, request):
        return render(request, 'admin/home_page.html')
class ucmp2(View):
    def get(self, request):
        return render(request, 'admin/ucmp2.html')
class usercomplaints(View):
    def get(self, request):
        return render(request, 'admin/usercomplaints.html')
class userdetails(View):
    def get(self, request):
        return render(request, 'admin/userdetails.html')
class users(View):
    def get(self, request):
        return render(request, 'admin/users.html')
    