from django.db import models

# Create your models here.

class Login_model(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    type=models.CharField(max_length=100, null=True, blank=True)
    status=models.CharField(max_length=100, null=True, blank=True)
    
    
class User_model(models.Model):
    LOGINID=models.ForeignKey(Login_model, on_delete=models.CASCADE, null=True, blank=True)
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    PIN = models.IntegerField(null=True, blank=True)
    profile= models.FileField(upload_to='userprofile/', null=True, blank=True)
    Phone_No = models.IntegerField(null=True, blank=True)
    
    
class Driver_model(models.Model):
    LOGINID=models.ForeignKey(Login_model, on_delete=models.CASCADE, null=True, blank=True)
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    PIN = models.IntegerField(null=True, blank=True)
    profile= models.FileField(upload_to='driverprofile/', null=True, blank=True)
    Phone_No = models.IntegerField(null=True, blank=True)
    vehicle_type = models.CharField(max_length=100, null=True, blank=True)
    License_no = models.CharField(max_length=100, null=True, blank=True)
    vehicle_no = models.CharField(max_length=100, null=True, blank=True)
    
class Feedback_model(models.Model):
    LOGINID=models.ForeignKey(Login_model, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    feedback = models.CharField(max_length=100, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

class Complanits_model(models.Model):
    LOGINID=models.ForeignKey(Login_model, on_delete=models.CASCADE, null=True, blank=True)
    complaint = models.CharField(max_length=100, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
     

    
        