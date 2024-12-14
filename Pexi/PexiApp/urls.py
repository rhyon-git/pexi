
from django.urls import path
from .views import *

urlpatterns = [
    path('',Login.as_view(),name='Login'),
    path('cmpmenu/',cmpmenu.as_view(),name='cmpmenu'),
    path('driver_details/',driver_details.as_view(),name='driver_details'),
    path('drivercmp/',drivercmp.as_view(),name='drivercmp'),
    path('drivers/',drivers.as_view(),name='driverse'),
    path('home_page/',home_page.as_view(),name='home_page'),
    path('ucmp2/',ucmp2.as_view(),name='ucmp2'),
    path('usercomplaints/',usercomplaints.as_view(),name='usercomplaints'),
    path('userdetails/',userdetails.as_view(),name='userdetails'),
    path('users/',users.as_view(),name='users'),
    path('display/',complaintdisplay.as_view(),name='display'),
    path('AllFeedback/',AllFeedback.as_view(),name='AllFeedback'),
    path('driverfeedback/',driverfeedback.as_view(),name='driverfeedback'),
    path('Userfeedback/',Userfeedback.as_view(),name='Userfeedback'),
    path('dcmp2/',dcmp2.as_view(),name='dcmp2'),
]
