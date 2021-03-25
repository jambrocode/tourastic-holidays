from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class packages(models.Model):
    package_id=models.AutoField
    package_name=models.CharField(max_length=100,default="")
    package_desc=models.TextField(default="")
    package_type=models.CharField(max_length=50,default="")
    package_images=models.ImageField(upload_to="home/pro_image",default="")
    package_categories=models.CharField(max_length=50,default="")
    package_duration=models.IntegerField(default=0)
    package_price=models.DecimalField(max_digits=20,decimal_places=2)
    package_hotels=models.TextField(default="")
    package_created=models.DateTimeField(default=timezone.now())
    package_createdby=models.CharField(max_length=50,default="")
    package_restaurant=models.TextField(default="")
    package_food=models.TextField(default="")
    package_services=models.TextField(default="")
    package_pickup=models.TextField(default="")
    package_drop=models.TextField(default="")
    package_video=models.FileField(upload_to="home/pro_image",default="")
    def __str__(self):
         return self.package_name

class order(models.Model):
    order_id=models.AutoField
    package = models.ForeignKey(packages, on_delete=models.SET_NULL, null=True)
    username=models.CharField(max_length=50,default="")
    passengers=models.IntegerField(default=0)
    daya_tour=models.IntegerField(default=0)
    date_tour=models.DateTimeField()
    enddate_tour=models.DateTimeField()
    order_status=models.CharField(max_length=50,default="")
    date_ordered=models.DateTimeField(default=timezone.now())
    def __str__(self):
         return self.order_id
## customize oder will be created after words
class hotels(models.Model):
    hotels_id=models.AutoField
    hotel_city=models.CharField(max_length=50,default="")
    hotel_country=models.CharField(max_length=100,default="")
    hotel_name=models.CharField(max_length=50,default="")
    hotel_image=models.ImageField(upload_to="home/pro_image",default="")
    hotel_description=models.TextField(default="")
    hotel_services=models.TextField(default="")
    hotels_price=models.DecimalField(max_digits=20,decimal_places=2)
    hotel_createdby=models.CharField(max_length=50,default="")
    hotel_no_of_rooms=models.IntegerField(default=0)
    hotel_type_room=models.CharField(max_length=20,default="")
    datetime=models.DateTimeField(default=datetime.now())
    hotel_updatedon=models.DateTimeField(default=timezone.now())

class transport(models.Model):
    transport_id=models.AutoField
    transport_mode=models.CharField(max_length=50,default="")
    service_name=models.CharField(max_length=100,default="")
    price_per_km=models.DecimalField(max_digits=20,decimal_places=2)
    added_by=models.CharField(max_length=50,default="")
    company_name=models.CharField(max_length=100,default="")
    datetime=models.DateTimeField(default=timezone.now())

# class food(models.Model):
#     food_id=models.AutoField
#     restaurant_name=models.CharField(max_length=100,default="")
#     food_desc=models.TextField
    
class userinfo(models.Model):
    users=models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    address=models.TextField(default="")
    mobile_no=models.IntegerField(max_length=10,default=0)
    pincode=models.IntegerField(max_length=5,default=0)
    country=models.CharField(max_length=50,default="")    
    datetime=models.DateTimeField(default=timezone.now())
class blogs(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=200,default="")
    images=models.ImageField(upload_to="home/pro_image",default="")
    description=models.TextField()
    createdat=models.DateTimeField(default=timezone.now())
    

class comments(models.Model):
    blog=models.ForeignKey(blogs,on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    commented_on=models.DateTimeField(default=timezone.now())
    comment=models.TextField()
    





    
    
    

    
