import uuid
from django.db import models

class NormalUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, verbose_name="firstname")
    lastname = models.CharField(max_length=50, unique=True)
    phone_num = models.IntegerField(default=0)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    last_login = models.DateTimeField(null=True, blank=True)
    is_normal_user = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'





class HotelOwner(models.Model):
    ho_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, verbose_name="firstname")
    lastname = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    last_login = models.DateTimeField(null=True, blank=True)
    is_normal_user = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'


class CabDriver(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    last_login = models.DateTimeField(null=True, blank=True)
    is_cab_driver = models.BooleanField(default=True)


class Appartment(models.Model):
    ap_id = models.AutoField(primary_key=True)
    appartmentname = models.CharField(max_length=50,verbose_name="name")
    propertytype = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    zipcode= models.IntegerField(max_length=50)
    year = models.IntegerField(max_length=50)
    propertysize = models.IntegerField(max_length=50)
    bedrooms = models.IntegerField(max_length=50)
    bathrooms = models.IntegerField(max_length=50)
    furnishing = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    rent = models.CharField(max_length=100)
    price= models.IntegerField(max_length=50)
    cimage = models.ImageField(upload_to='images',default="")
    propdesc = models.CharField(max_length=100)
    status= models.BooleanField(default="1")
    USERNAME_FIELD = 'username'

class appartment_booking(models.Model):
    b_id = models.AutoField(primary_key=True)
    appartment_name = models.CharField(max_length=50,default="")
    appartment_id = models.CharField(max_length=50,default="")
    user = models.CharField(max_length=50,default="")
    user_id = models.CharField(max_length=50,default="")
    price= models.CharField(max_length=50)
    start_date=models.DateField()
    end_date = models.DateField()
    status= models.BooleanField(default=0)
    payment_status=models.BooleanField(default=0)


class appartment_bookings(models.Model):
    b_id = models.AutoField(primary_key=True)
    appartment_name = models.CharField(max_length=50,default="")
    appartment_id = models.CharField(max_length=50,default="")
    user = models.CharField(max_length=50,default="")
    user_id = models.CharField(max_length=50,default="")
    price= models.CharField(max_length=50)
    date=models.DateField()
    status= models.BooleanField(default=0)
    payment_status=models.BooleanField(default=0)