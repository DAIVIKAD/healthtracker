from re import T
from urllib import request
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import  Person , Hospital,  Appointment,  Doctor_detail, Pharmacy, Fees, Invoice, Fees_type, Insurance, Laboratory, Feed_back, Result_test, Health_test
from .serializers import  PersonSerializer, HospitalSerializer,  AppointmentSerializer,  Doctor_detailSerializer, PharmacySerializer, FeesSerializer, InvoiceSerializer, Fees_typeSerializer, InsuranceSerializer, LaboratorySerializer, Feed_backSerializer, Result_testSerializer, Health_testSerializer

class API_Person(APIView):
   def get(self, request):
       Persons = Person.objects.all().order_by('id')
       serializer = PersonSerializer(Persons, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer = PersonSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


@api_view(['GET','PUT'])
def Person_detail(request,pk):
    try:
        Persons = Person.objects.get(pk=pk)
    except Persons.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializer = PersonSerializer(Persons)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonSerializer(Persons,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         





class API_Hospital(APIView):
   def get(self, request):
       Hospitals = Hospital.objects.all().order_by('id')
       serializer = HospitalSerializer(Hospitals, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer = HospitalSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['GET','PUT'])
def Hospital_detail(request,pk):
    try:
        Hospitals = Hospital.objects.get(pk=pk)
    except Hospitals.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializer = HospitalSerializer(Hospitals)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HospitalSerializer(Hospitals,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         



class API_Appointment(APIView):
   def get(self, request):
       Appointments = Appointment.objects.all().order_by('id')
       serializer = AppointmentSerializer(Appointments, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer = AppointmentSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT'])
def Appointment_detail(request,pk):
    try:
        Appointments = Appointment.objects.get(pk=pk)
    except Appointments.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializer = AppointmentSerializer(Appointments)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AppointmentSerializer(Appointments,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         

            

class API_Doctor_detail(APIView):
     def get(self, request):
       Doctor_details = Doctor_detail.objects.all().order_by('id')
       serializer = Doctor_detailSerializer(Doctor_details, many=True)
       return Response(serializer.data)

     def  post(self, request):
        serializer = Doctor_detailSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

@api_view(['GET','PUT'])
def Doctor_detail_detail(request,pk):
    try:
        Doctor_details = Doctor_detail.objects.get(pk=pk)
    except Doctor_details.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializer = Doctor_detailSerializer(Doctor_details)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Doctor_detailSerializer(Doctor_details,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         


class API_Pharmacy(APIView):
   def get(self, request):
       Pharmacys = Pharmacy.objects.all().order_by('id')
       serializer = PharmacySerializer(Pharmacys, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer = PharmacySerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


@api_view(['GET','PUT'])
def Pharmacy_detail(request,pk):
    try:
        Pharmacys = Pharmacy.objects.get(pk=pk)
    except Pharmacys.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializer = PharmacySerializer(Pharmacy)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PharmacySerializer(Pharmacys,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class API_Fees(APIView):
     def get(self, request):
       Feess = Fees.objects.all().order_by('id')
       serializer = FeesSerializer(Feess, many=True)
       return Response(serializer.data)

     def  post(self, request):
        serializer = FeesSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

@api_view(['GET','PUT'])
def Fees_detail(request,pk):
    try:
        Feess = Fees.objects.get(pk=pk)
    except Feess.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializer = FeesSerializer(Feess)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FeesSerializer(Feess,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         


class API_Invoice(APIView):
     def get(self, request):
       Invoices = Invoice.objects.all().order_by('id')
       serializer = InvoiceSerializer(Invoices, many=True)
       return Response(serializer.data)

     def  post(self, request):
        serializer = InvoiceSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

@api_view(['GET','PUT'])
def Invoice_detail(request,pk):
    try:
        Invoices = Invoice.objects.get(pk=pk)
    except Invoices.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializer = InvoiceSerializer(Invoices)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InvoiceSerializer(Invoices,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         
   
class API_Fees_type(APIView):
   def get(self, request):
       Fees_types = Fees_type.objects.all().order_by('id')
       serializer = Fees_typeSerializer(Fees_types, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer = Fees_typeSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


@api_view(['GET','PUT'])
def Fees_type_detail(request,pk):
    try:
        Fees_types = Fees_type.objects.get(pk=pk)
    except Fees_types.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializer = Fees_typeSerializer(Fees_types)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Fees_typeSerializer(Fees_type,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class API_Insurance(APIView):
   def get(self, request):
       Insurances = Insurance.objects.all().order_by('id')
       serializer = InsuranceSerializer(Insurance, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer = InsuranceSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

@api_view(['GET','PUT'])
def Insurance_detail(request,pk):
    try:
        Insurances = Insurance.objects.get(pk=pk)
    except Insurances.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializer = InsuranceSerializer(Insurances)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InsuranceSerializer(Insurances,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

class API_Laboratory(APIView):
   def get(self, request):
       Laboratorys =  Laboratory.objects.all().order_by('id')
       serializer =  LaboratorySerializer( Laboratorys, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer =  LaboratorySerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET','PUT'])
def Laboratory_detail(request,pk):
    try:
        Laboratorys = Laboratory.objects.get(pk=pk)
    except Laboratorys.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializer = LaboratorySerializer(Laboratory)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LaboratorySerializer(Laboratorys,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         


class API_Feed_back(APIView):
   def get(self, request):
       Feed_backs =  Feed_back.objects.all().order_by('id')
       serializer =  Feed_backSerializer( Feed_backs, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer =  Feed_backSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


@api_view(['GET','PUT'])
def Feed_back_detail(request,pk):
    try:
        Feed_backs = Feed_back.objects.get(pk=pk)
    except Feed_backs.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializer = Feed_backSerializer(Feed_backs)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Feed_backSerializer(Feed_back,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         


class API_Result_test(APIView):
   def get(self, request):
       Result_tests =  Result_test.objects.all().order_by('id')
       serializer =  Result_testSerializer( Result_tests, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer =  Result_testSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['GET','PUT'])
def Result_test_detail(request,pk):
    try:
        Result_tests = Result_test.objects.get(pk=pk)
    except Result_tests.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializer = Result_testSerializer(Result_tests)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Result_testSerializer(Result_test,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         


class API_Health_test(APIView):
   def get(self, request):
       Health_tests =  Health_test.objects.all().order_by('id')
       serializer =  Health_testSerializer(Health_tests, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer =  Health_testSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET','PUT'])
def Health_test_detail(request,pk):
    try:
        Health_tests = Health_test.objects.get(pk=pk)
    except Health_test.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializer = Health_testSerializer(Health_tests)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Health_testSerializer(Health_tests,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         


     
# Create your views here.

