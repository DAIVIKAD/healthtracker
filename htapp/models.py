
import re
from sre_parse import Verbose
from telnetlib import STATUS
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.


class AppUserManager(BaseUserManager):

    def create_superuser(self, email, branch_code, staff_id, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user (email, branch_code, staff_id, password, **other_fields)

    def create_user( self, email, branch_code, staff_id, password, **other_fields):
        if not email:
            raise ValueError('You must provide a valid email address')

        email = self.normalize_email(email)
        user = self.model(email = email, branch_code = branch_code, staff_id = staff_id, ** other_fields)
        user.set_password(password)
        user.save()
        return user


class AppUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=80, null=True, verbose_name = "First Name")
    last_name = models.CharField(max_length=80, null=True, verbose_name = "Last Name")
    branch_code = models.CharField(max_length=20, null=True, verbose_name = "Branch Code")
    staff_id =  models.CharField(max_length=20, null=True, verbose_name = "Staff Id")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    start_date = models.DateTimeField(default=timezone.now)

    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['branch_code', 'staff_id']

    def __str__(self):
        return self.staff_id

       

class Person(models.Model):

    Gender = (('M','Male'),
        ('F','Female'),
        ('M','Male'),
        ('O','Other'))

    Ratings = (('1', '*'),
        ('2','**'),
        ('3','***'),
        ('4','****'),
        ('5','*****'))

    Status = (('DEAD','Dead'),
        ('SICK','sick'),
        ('HEALTHY','Healthy'),
        ('UNHEALTHY','Unhealthy'))



    Person_name = models.CharField(max_length=100,blank=True, null=True, verbose_name="Person name")
    Person_address = models.CharField(max_length=120, blank=True, null=True, verbose_name="Person address")
    Person_pri_phone= models.CharField(max_length=13, blank=True, null=True, verbose_name="Person pri_phone")
    Person_sec_phone = models.CharField(max_length=13, blank=True, null=True, verbose_name="Person sec_phone")
    Person_dob = models.DateField(blank=True,null=True,verbose_name="DOB")
    Person_gender = models.CharField(max_length=1, choices= Gender, default='M', verbose_name="Gender")
    Person_email = models.EmailField(max_length=100, blank=True, null=True, verbose_name="Email Address")
    Person_status = models.CharField(max_length=10, blank=True,choices=Status, default='HEALTHY', null=True, verbose_name="health status")
    Person_notes = models.CharField(max_length=200, blank=True, null=True, verbose_name="health notes")
    Person_rating = models.CharField(max_length=1, choices=Ratings, default='5', verbose_name="Rating")
    Added_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='ADDED BY' )
    Added_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='ADDED DATE/TIME')
    updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='UPDATED BY')
    updated_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='UPDATE DATE/TIME')
    Person_status = models.CharField(max_length=20, blank=True, null=True, verbose_name="health status")
    Person_notes = models.CharField(max_length=200, blank=True, null=True, verbose_name="health notes")
    Person_rating = models.CharField(max_length=1, choices=Ratings,default=5,verbose_name="Rating")

    

    def __str__(self):
        return self.Person_name




class Hospital(models.Model):

    Hospital_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='HOSPITAL NAME')
    Hospital_address = models.CharField(max_length=100, blank=True, null=True, verbose_name='HOSPITAL ADDRESS')
    Contact_details = models.CharField(max_length=100,blank=True, null=True, verbose_name='CONTACT DETAILS')
    Hospital_email = models.EmailField(max_length=100, blank=True, null=True, verbose_name="Email Address")
    Added_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='ADDED BY' )
    Added_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='ADDED DATE/TIME')
    Updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='UPDATED BY')
    Updated_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='UPDATE DATE/TIME')

    def __str__(self):
        return self.Hospital_name


class Doctor_detail(models.Model):


    Specialized = (('1','CARDIOLOGIST'),
        ('2','AUDIOLOGIST'),
        ('3','DENTIST'),
        ('4','ENT SPECIALIST'),
        ('5','GYNAECOLOGIS'),
        ('6','ORTHOPAEDIC SURGEON'),
        ('7','paediatrician'),
        ('8','NEUROLOGIST'))

    Doctor_name = models.CharField(max_length=100, blank=True, null=True, verbose_name= "DOCTER NAME")
    Specialized_of = models.CharField(max_length=100, choices= Specialized, default='select', verbose_name="SPECIALIZED OF")
    E_email = models.EmailField(max_length=100, blank=True, null=True, verbose_name="Email ")
    Qualification = models.CharField(max_length=100, blank=True, null=True, verbose_name='Qualification')
    Added_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='ADDED BY' )
    Added_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='ADDED DATE/TIME')
    Updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='UPDATED BY')
    Updated_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='UPDATE DATE/TIME')

    def __str__(self):
        return self.Doctor_name
        
class Appointment(models.Model):
    
    Person_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='PERSON NAME')
    Docter_name = models.ForeignKey(Doctor_detail, on_delete=models.PROTECT, null=True, verbose_name="DOCTER NAME")
    Date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name=' NEED ON DATE/TIME')
    Health_condition = models.CharField(max_length=100, blank=True, null=True, verbose_name='HEALTH CONDITION')
    Appointment_notes = models.CharField(max_length=200, blank=True, null=True, verbose_name='APPOINTMENT NOTES')
  
    

    def __str__(self):
        return self.Person_name


class Pharmacy(models.Model):

    Pharmacy_name = models.CharField(max_length=100, blank=False, null=True, verbose_name='PHARMACY NAME')
    Pharmacy_address = models.CharField(max_length=100, blank=True, null=True, verbose_name='PHARMACY ADDRESS')
    Pharmacy_items = models.CharField(max_length=100, blank=True, null=True, verbose_name='PHARMACY ITEMS')
    Syrup = models.CharField(max_length=100, blank=True, null=True, verbose_name='SYRUP')
    Syrup_cost = models.IntegerField(blank=True, null=True, verbose_name='COST')
   
    Ointment = models.CharField(max_length=100, blank=True, null=True, verbose_name='OINTMENT')
    ointment_cost = models.IntegerField(blank=True, null=True, verbose_name='OINTMENT COST')
    Lotions = models.CharField(max_length=100, blank=True, null=True, verbose_name='LOTIONS')
    Lotion_Cost = models.IntegerField(blank=True, null=True, verbose_name='LOTION COST')
    Total_Cost = models.IntegerField(blank=True, null=True, verbose_name='TOTAL COST')
    Added_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='ADDED BY' )
    Added_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='ADDED DATE/TIME')
    Updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='UPDATED BY')
    Updated_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='UPDATE DATE/TIME')

    def __str__(self):
        return self.Pharmacy_name

class Fees(models.Model):

    Person_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='PERSON NAME')
    Paid = models.IntegerField(blank=True, null=True, verbose_name='PAID')
    Pending = models.IntegerField(blank=True, null=True, verbose_name='PENDING')
    Invoice_id = models.IntegerField(blank=True, null=True, verbose_name='INVOICE ID')
    Added_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='ADDED BY' )
    Added_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='ADDED DATE/TIME')
    Updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='UPDATED BY')
    Updated_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='UPDATE DATE/TIME')

    def __str__(self):
        return self.Person_name 

class Invoice(models.Model):

    Person_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='PERSON NAME')
    Invoice_number = models.IntegerField(blank=True, null=True, verbose_name='INVOICE NUMBER')
    Company_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='COMPANY NAME')
    Invoice_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='INVOICE DATE/TIME')
    Invoice_due_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='INVOICE DUE DATE/TIME')
    Description = models.CharField(max_length=200, blank=True, null=True, verbose_name='DESCRIPTION')
    Quality = models.IntegerField(blank=True, null=True, verbose_name='QUALITY')
    Price = models.IntegerField(blank=True, null=True, verbose_name='PRICE')
    Tax = models.IntegerField(blank=True, null=True, verbose_name='TAX')
    Amount = models.IntegerField(blank=True, null=True, verbose_name='AMOUNT')
    Added_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='ADDED BY' )
    Added_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='ADDED DATE/TIME')
    Updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='UPDATED BY')
    Updated_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='UPDATE DATE/TIME')

    def __str__(self):
        return self.Person_name


class Fees_type(models.Model):

    Person_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='PERSON NAME')
    Cunsultancy_fees = models.IntegerField(blank=True, null=True, verbose_name='CONSULTANCY FEES')
    Laboratory_fees = models.IntegerField(blank=True, null=True, verbose_name='LABORATORY FEES')
    Pharmacy_fees = models.IntegerField(blank=True, null=True, verbose_name='PHARMACY FEES')
    Other_fees = models.IntegerField(blank=True, null=True, verbose_name='OTHER FEES')
    Other_fees_desc = models.CharField(max_length=200,blank=True, null=True, verbose_name='OTHER FEES DESCRIPTION')
    Grand_total = models.IntegerField(blank=True, null=True, verbose_name='GRAND TOTAL')
    Paid_through = models.CharField(max_length=100, blank=True, null=True, verbose_name='PAID THROUGH')
    Added_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='ADDED BY' )
    Added_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='ADDED DATE/TIME')
    Updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='UPDATED BY')
    Updated_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='UPDATE DATE/TIME')


    def __str__(self):
        return self.Person_name


class Insurance(models.Model):

    Insurance_type = models.CharField(max_length=100, blank=True, null=True, verbose_name='INSURANCE TYPE')
    Insurance_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='INSURANCE NAME')
    Valid_from = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='VALID FROM')
    Valid_to = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='VALID TO')
    Added_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='ADDED BY' )
    Added_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='ADDED DATE/TIME')
    Updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='UPDATED BY')
    Updated_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='UPDATE DATE/TIME')

    def __str__(self):
        return self.Insurance_type


class Laboratory(models.Model):

    Laboratory_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='LABORATORY NAME')
    Address = models.CharField(max_length=200, blank=True, null=True, verbose_name='ADDRESS')
    Pin_code = models.CharField(max_length=6,blank=True, null=True, verbose_name='PIN CODE')
    Test = models.CharField(max_length=100, blank=True, null=True, verbose_name='TEST')
    Availability = models.CharField(max_length=100, blank=True, null=True, verbose_name='AVAILABILITY')
    Reffered_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='REFFERED BY')
    Added_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='ADDED BY' )
    Added_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='ADDED DATE/TIME')
    Updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='UPDATED BY')
    Updated_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='UPDATE DATE/TIME')

    def __str__(self):
        return self.Laboratory_name


class Feed_back(models.Model):

    Rating = (('1', '*'),
        ('2','**'),
        ('3','***'),
        ('4','****'),
        ('5','*****'))

    Description = models.CharField(max_length=100, blank=True, null=True, verbose_name='Description')
    Rating = models.CharField(max_length=1, choices=Rating, default='5', verbose_name="Rating")
    Person_name = models.ForeignKey(Person, on_delete=models.PROTECT, null=True, verbose_name="PERSON NAME")

    def __str__(self):
        return self.Description

class Result_test(models.Model):
    
    Name_test    =  models.CharField(max_length=50, blank=False, null=True, verbose_name='NAME OF TEST') 
    Normal_range =  models.CharField(max_length=50, blank=True, null=True, verbose_name='NORMAL RANGE') 
    Result_report = models.ImageField(upload_to='test_result/', null=True, blank=True)
    X_ray = models.ImageField(upload_to='X_ray/', null=True, blank=True)
    Result_value =  models.CharField(max_length=50, blank=True, null=True, verbose_name='RESULT VALUE')
   
    def __str__(self):

       return self.Name_test


class Health_test(models.Model):

    Person_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='PERSON NAME')
    Ref_by_doc   = models.ForeignKey(Doctor_detail, on_delete=models.PROTECT, null=True, verbose_name='REF BY DOC') 
    Name_test    =  models.CharField(max_length=50, blank=True, null=True, verbose_name='NAME OF TEST') 
    Date_test =  models.DateTimeField(max_length=50, blank=True, null=True, verbose_name='DATE OF TEST') 
    Date_result =  models.DateTimeField(max_length=50, blank=True, null=True, verbose_name='RESULT DATE ')
    Prescribed_date = models.DateTimeField(max_length=50, blank=True, null=True, verbose_name='PRESCRIBED DATE ')
    Description = models.CharField(max_length=50, blank=True, null=True, verbose_name='DESCRIPTION')

    def __str__(self):

       return self. Person_name






















        
