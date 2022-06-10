from distutils.command.upload import upload
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
    Person_status = models.CharField(max_length=1, blank=True,choices=Status, default='HEALTHY', null=True, verbose_name="health status")
    Person_notes = models.CharField(max_length=200, blank=True, null=True, verbose_name="health notes")
    Person_rating = models.CharField(max_length=1, choices=Ratings, default='5', verbose_name="Rating")
    Added_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='ADDED BY' )
    Added_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='ADDED DATE/TIME')
    Updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='UPDATED BY')
    Updated_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='UPDATE DATE/TIME')
    

    def __str__(self):
        return self.Person_name

class Test(models.Model):
    Test_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='TEST NAME')
    Test_description = models.CharField(max_length=200, blank=True, null=True, verbose_name='TEST DESCRIPTION')
    Test_pre_condition = models.CharField(max_length=200, blank=True, null=True, verbose_name='TEST PRE-CONDITION')
    Test_notes = models.CharField(max_length=200, blank=True, null=True, verbose_name='TEST NOTES')
    Added_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='ADDED BY' )
    Added_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='ADDED DATE/TIME')
    Updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='UPDATED BY')
    Updated_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='UPDATE DATE/TIME')


    def __str__(self):
        return self.Test_name

class Appointment(models.Model):
    Person_name = models.ForeignKey(Person, on_delete=models.PROTECT, null=True, verbose_name="PERSON NAME")
    Doctor_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='DOCTOR NAME')
    Date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='DATE/TIME')
    Health_condition = models.CharField(max_length=100, blank=True, null=True, verbose_name='HEALTH CONDITION')
    Appointment_time_duration = models.IntegerField(blank=True, null=True, verbose_name='APPOINTMENT TIME DURATION')
    Appointment_notes = models.CharField(max_length=200, blank=True, null=True, verbose_name='APPOINTMENT NOTES')
    Added_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='ADDED BY' )
    Added_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='ADDED DATE/TIME')
    Updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='UPDATED BY')
    Updated_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='UPDATE DATE/TIME')
    

    def __str__(self):
        return self.Person_name

class Test_result(models.Model):
    Test_name = models.ForeignKey(Test, on_delete=models.PROTECT, null=True, verbose_name="PERSON NAME FOR RESULT")
    Unit_of_measure = models.CharField(max_length=50, blank=True, null=True, verbose_name='UNIT OF MEASURE')
    Normal_range =  models.CharField(max_length=50, blank=True, null=True, verbose_name='NORMAL RANGE') 
    Result_value =  models.CharField(max_length=50, blank=True, null=True, verbose_name='RESULT VALUE')
    X_ray = models.ImageField(upload_to='x_ray/', null=True, blank=True)
    Result_report = models.ImageField(upload_to='test_result', null=True, blank=True)
    Added_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='ADDED BY' )
    Added_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='ADDED DATE/TIME')
    Updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='UPDATED BY')
    Updated_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='UPDATE DATE/TIME')

    def __str__(self):
        return self.Test_name

class Hospital(models.Model):
    Hospital_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='HOSPITAL NAME')
    Hospital_address = models.CharField(max_length=100, blank=True, null=True, verbose_name='HOSPITAL ADDRESS')
    Contact_details = models.IntegerField(blank=True, null=True, verbose_name='CONTACT DETAILS')
    Added_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='ADDED BY' )
    Added_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='ADDED DATE/TIME')
    Updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='UPDATED BY')
    Updated_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='UPDATE DATE/TIME')

    def __str__(self):
        return self.Hospital_name

class Doctor_details(models.Model):


    Specialized = (('1','CARDIOLOGIST'),
        ('2','AUDIOLOGIST'),
        ('3','DENTIST'),
        ('4','ENT SPECIALIST'),
        ('5','GYNAECOLOGIS'),
        ('6','ORTHOPAEDIC SURGEON'),
        ('7','paediatrician'),
        ('8','NEUROLOGIST'))

    Doctor_name = models.ForeignKey(Appointment, on_delete=models.PROTECT, null=True, verbose_name="DOCTOR NAME")
    Specialized_of = models.CharField(max_length=1, choices=1, default='select', verbose_name="SPECIALIZED OF")
    E_email = models.EmailField(max_length=100, blank=True, null=True, verbose_name="Email ")
    Qualification = models.CharField(max_length=100, blank=True, null=True, verbose_name='Qualification')
    Added_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='ADDED BY' )
    Added_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='ADDED DATE/TIME')
    Updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='UPDATED BY')
    Updated_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='UPDATE DATE/TIME')

    def __str__(self):
        return self.Doctor_name

class Pharmacy(models.Model):

    Pharmacy_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='PHARMACY NAME')
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

    Paid = models.IntegerField(blank=True, null=True, verbose_name='PAID')
    Pending = models.IntegerField(blank=True, null=True, verbose_name='PENDING')
    Invoice_id = models.IntegerField(blank=True, null=True, verbose_name='INVOICE ID')
    Added_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='ADDED BY' )
    Added_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='ADDED DATE/TIME')
    Updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='UPDATED BY')
    Updated_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='UPDATE DATE/TIME')

    def __str__(self):
        return self.Paid

class Invoice(models.Model):

    Invoice_number = models.IntegerField(blank=True, null=True, verbose_name='INVOICE NUMBER')
    Company_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='COMPANY NAME')
    Invoice_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='INVOICE DATE/TIME')
    Invoice_due_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='INVOICE DUE DATE/TIME')
    Description = models.CharField(max_length=100, blank=True, null=True, verbose_name='DESCRIPTION')
    Quality = models.IntegerField(blank=True, null=True, verbose_name='QUALITY')
    Price = models.IntegerField(blank=True, null=True, verbose_name='PRICE')
    Tax = models.IntegerField(blank=True, null=True, verbose_name='TAX')
    Amount = models.IntegerField(blank=True, null=True, verbose_name='AMOUNT')
    Added_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='ADDED BY' )
    Added_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='ADDED DATE/TIME')
    Updated_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='UPDATED BY')
    Updated_date_time = models.DateTimeField(max_length=100, blank=True, null=True, verbose_name='UPDATE DATE/TIME')

    def __str__(self):
        return self.Invoice_number

        










        
