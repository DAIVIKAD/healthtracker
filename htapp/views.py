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
       serializer = HospitalSerializer(Hospital, many=True)
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
    except Hospital.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializers = HospitalSerializer(Hospital)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HospitalSerializer(Hospital,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         



class API_Appointment(APIView):
   def get(self, request):
       Appointment = Appointment.objects.all().order_by('id')
       serializer = AppointmentSerializer(Appointment, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer = AppointmentSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT'])
def Appointment_detail(request,pk):
    try:
        Appointment = appointment.objects.get(pk=pk)
    except Appointment.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializers = AppointmentSerializer(Appointment)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializers = AppointmentSerializer(Appointment,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         

            

class API_Doctor_detail(APIView):
     def get(self, request):
       Doctor_detail = Doctor_detail.objects.all().order_by('id')
       serializer = Doctor_detailSerializer(Doctor_detail, many=True)
       return Response(serializer.data)

     def  post(self, request):
        serializer = Doctor_detailSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  

@api_view(['GET','PUT'])
def Doctor_detail_detail(request,pk):
    try:
        Doctor_detail = doctor_detail.objects.get(pk=pk)
    except Doctor_detail.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializers = Doctor_detailSerializer(Doctor_detail)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializers = Doctor_detailSerializer(Doctor_detail,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         


class API_Pharmacy(APIView):
   def get(self, request):
       Pharmacy = Pharmacy.objects.all().order_by('id')
       serializer = PharmacySerializer(Pharmacy, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer = PharmacySerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  


@api_view(['GET','PUT'])
def Pharmacy_detail(request,pk):
    try:
        Pharmacy = pharmacy.objects.get(pk=pk)
    except Pharmacy.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializers = PharmacySerializer(Person)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializers = PharmacySerializer(Pharmacy,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class API_Fees(APIView):
     def get(self, request):
       Fees = Fees.objects.all().order_by('id')
       serializer = FeesSerializers(Fees, many=True)
       return Response(serializer.data)

     def  post(self, request):
        serializer = FeesSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  

@api_view(['GET','PUT'])
def Fees_detail(request,pk):
    try:
        Fees = Fees.objects.get(pk=pk)
    except Fees.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializers = FeesSerializer(Fees)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializers = FeesSerializer(Fees,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         


class API_Invoice(APIView):
     def get(self, request):
       Invoice = Invoice.objects.all().order_by('id')
       serializer = InvoiceSerializer(Invoice, many=True)
       return Response(serializer.data)

     def  post(self, request):
        serializer = InvoiceSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  

@api_view(['GET','PUT'])
def Invoice_detail(request,pk):
    try:
        Invoice = fees.objects.get(pk=pk)
    except Fees.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializers = InvoiceSerializer(Invoice)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializers = InvoiceSerializer(Invoice,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         
   
class API_Fees_type(APIView):
   def get(self, request):
       Fees_type = Fees_type.objects.all().order_by('id')
       serializer = Fees_typeSerializer(Fees_type, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer = Fees_typeSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  


@api_view(['GET','PUT'])
def Fees_type_detail(request,pk):
    try:
        Fees_type = fees_type.objects.get(pk=pk)
    except Fees_type.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializers = Fees_typeSerializer(Fees_type)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializers = Fees_typeSerializer(Fees_type,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class API_Insurance(APIView):
   def get(self, request):
       Insurance = Insurance.objects.all().order_by('id')
       serializer = InsuranceSerializers(Insurance, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer = InsuranceSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  

@api_view(['GET','PUT'])
def Insurance_detail(request,pk):
    try:
        Insurance = insurance.objects.get(pk=pk)
    except Insurance.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializers = InsuranceSerializer(Insurance)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializers = InsuranceSerializer(Insurance,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

class API_Laboratory(APIView):
   def get(self, request):
       Laboratory =  Laboratory.objects.all().order_by('id')
       serializer =  LaboratorySerializer( Laboratory, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer =  LaboratorySerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST) 

@api_view(['GET','PUT'])
def Laboratory_detail(request,pk):
    try:
        Laboratory = laboratory.objects.get(pk=pk)
    except Laboratory.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializers = LaboratorySerializer(Laboratory)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializers = LaboratorySerializer(Laboratory,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         


class API_Feed_back(APIView):
   def get(self, request):
       Feed_back =  Feed_back.objects.all().order_by('id')
       serializer =  Feed_backSerializers( Feed_back, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer =  Feed_backSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  


@api_view(['GET','PUT'])
def Feed_back_detail(request,pk):
    try:
        Feed_back= feed_back.objects.get(pk=pk)
    except Feed_back.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializers = Feed_backSerializer(Feed_back)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializers = Feed_backSerializer(Feed_back,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         


class API_Result_test(APIView):
   def get(self, request):
       Result_test =  Result_test.objects.all().order_by('id')
       serializer =  Result_testSerializer( Result_test, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer =  Result_testSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)    

@api_view(['GET','PUT'])
def Result_test_detail(request,pk):
    try:
        Result_test = result_test.objects.get(pk=pk)
    except Result_test.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializers = Result_testSerializer(Result_test)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializers = Result_testSerializer(Result_test,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         


class API_Health_test(APIView):
   def get(self, request):
       Health_test =  Health_test.objects.all().order_by('id')
       serializer =  Health_testSerializers(Health_test , many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer =  Health_testSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST) 


@api_view(['GET','PUT'])
def Health_test_detail(request,pk):
    try:
        Health_test = health_test.objects.get(pk=pk)
    except Health_test.DoesNotExist:
        return Response(status=status.HTTP_400_NO_FOUND)

    if request.method =='GET':
       serializers = Health_testSerializer(Health_test)
       return Response(serializer.data)

    elif request.method == 'PUT':
        serializers = Health_testSerializer(Health_test,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         


     
# Create your views here.

