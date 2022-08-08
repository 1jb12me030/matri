
from django.contrib.auth.models import User
from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from app.manager import *

# Create your models here.

class BaseModel(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class UserRegister(AbstractUser):
    username = None
    choice_gender=(('Male','Male'),('Female','Female'))
    profile=(('Self','Self'),('Parents','Parents'),('Sibling','Sibling'))
    mobile_number=models.CharField(max_length=15,unique=True)
    is_verified=models.BooleanField(default=False)
    gender=models.CharField(max_length=50,choices=choice_gender)
    father_name=models.CharField(max_length=100)
    mother_name=models.CharField(max_length=100)
    education=models.CharField(max_length=100)
    dob=models.DateField(max_length=100)
    pic=models.ImageField(null=True,blank=True)
    profile_created_by=models.CharField(max_length=100,choices=profile)

    USERNAME_FIELD='mobile_number'
    REQUIRED_FIELDS=[]
    objects=UserManager()

    def __str__(self):
        return self.mobile_number
class Package(BaseModel):
    amount=models.IntegerField()
    member=[('Gold','Gold'),('Silver','Silver'),('Diamond','Diamond')]
    membership=models.CharField(max_length=100,choices=member)

class PaymentDetails(BaseModel):

    """Stores payment details"""
    transaction_id=models.CharField(null=True,blank=True,max_length=100)
    order_id=models.CharField(null=True,blank=True,max_length=100)
    payment_signature=models.CharField(null=True,blank=True,max_length=100)
    is_paid=models.BooleanField(default=False)
    register=models.ForeignKey(UserRegister,on_delete=models.CASCADE)
    package=models.ForeignKey(Package,null=True,blank=True,on_delete=models.CASCADE)

# class Registration(BaseModel):

#     """Stores user """
#     choice_gender=(('Male','Male'),('Female','Female'))
#     profile=(('Self','Self'),('Parents','Parents'),('Sibling','Sibling'))
    
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     mobile_number=models.CharField(max_length=15)
#     gender=models.CharField(max_length=50,choices=choice_gender)
#     father_name=models.CharField(max_length=100)
#     mother_name=models.CharField(max_length=100)
#     education=models.CharField(max_length=100)
#     dob=models.DateField(max_length=100)
#     pic=models.ImageField(null=True,blank=True)
#     profile_created_by=models.CharField(max_length=100,choices=profile)

#     def __str__(self):
#         return self.name

# class PersonalDetails(BaseModel):

#     """Stores personal information"""

#     choice_gender=(('Male','Male'),('Female','Female'))
#     profile=(('Self','Self'),('Parents','Parents'),('Sibling','Sibling'))
#     gender=models.CharField(max_length=50,choices=choice_gender)
#     father_name=models.CharField(max_length=100)
#     mother_name=models.CharField(max_length=100)
#     education=models.CharField(max_length=100)
#     dob=models.DateField(max_length=100)
#     pic=models.ImageField(null=True,blank=True)
#     profile_created_by=models.CharField(max_length=100,choices=profile)
#     def __str__(self):
#         return self.father_name
