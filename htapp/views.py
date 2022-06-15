from re import T
from django.shortcuts import render
from rest_framework import Permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIview
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_password
from .models import  Person , Hospital,  Appointment,  Doctor_detail, Pharmacy, Fees, Invoice, Fees_type, Insurance, Laboratory, Feed_back, Result_test, Health_test
from .serializers import Personserializers , Hospitalserializers,  Appointmentserializers,  Doctor_detailserializers, Pharmacyserializers, Feesserializers, Invoiceserializers, Fees_typeserializers, Insuranceserializers, Laboratoryserializers, Feed_backserializers, Result_testserializers, Health_testserializers

class API_Person(APIview):
   def get(self, request):
       Person = Person.objects.all().order_by('id')
       serializer = PersonSerializers(Person, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer = PersonSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  


class API_Hospital(APIview):
   def get(self, request):
       Hospital = Hospital.objects.all().order_by('id')
       serializer = HospitalSerializers(Hospital, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer = HospitalSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)    


class API_Appointment(APIview):
   def get(self, request):
       Appointment = Appointment.objects.all().order_by('id')
       serializer = AppointmentSerializers(Appointment, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer = AppointmentSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)    

class API_Doctor_detail(APIview):
     def get(self, request):
       Doctor_detail = Doctor_detail.objects.all().order_by('id')
       serializer = Doctor_detailSerializers(Doctor_detail, many=True)
       return Response(serializer.data)

     def  post(self, request):
        serializer = Doctor_detailSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  

class API_Pharmacy(APIview):
   def get(self, request):
       Pharmacy = Pharmacy.objects.all().order_by('id')
       serializer = PharmacySerializers(Pharmacy, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer = PharmacySerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  



class API_Fees(APIview):
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


class API_Invoice(APIview):
     def get(self, request):
       Invoice = Invoice.objects.all().order_by('id')
       serializer = InvoiceSerializers(Invoice, many=True)
       return Response(serializer.data)

     def  post(self, request):
        serializer = InvoiceSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  
   
class API_Fees_type(APIview):
   def get(self, request):
       Fees_type = Fees_type.objects.all().order_by('id')
       serializer = Fees_typeSerializers(Fees_type, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer = Fees_typeSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  

class API_Insurance(APIview):
   def get(self, request):
       Insurance = Fees_type.objects.all().order_by('id')
       serializer = InsuranceSerializers(Insurance, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer = InsuranceSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  

class API_Laboratory(APIview):
   def get(self, request):
       Laboratory =  Laboratory.objects.all().order_by('id')
       serializer =  LaboratorySerializers( Laboratory, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer =  LaboratorySerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST) 


class API_Feed_back(APIview):
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

class API_Result_test(APIview):
   def get(self, request):
       Result_test =  Result_test.objects.all().order_by('id')
       serializer =  Result_testSerializers( Result_test, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer =  Result_testSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)    

class API_Health_test(APIview):
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



     
# Create your views here.

