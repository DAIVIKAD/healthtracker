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
       serializer = Personserializers(Person, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer = PersonSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  


class API_Hospital(APIview):
   def get(self, request):
       Person = Hospital.objects.all().order_by('id')
       serializer = Hospitalserializers(Hospital, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer = HospitalSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)    


class API_Appointment(APIview):
   def get(self, request):
       Person = Appointment.objects.all().order_by('id')
       serializer = Appointmentserializers(Appointment, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer = AppointmentSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)    

class API_Doctor_detail(APIview):
   def get(self, request):
       Person = Appointment.objects.all().order_by('id')
       serializer = Appointmentserializers(Doctor_details, many=True)
       return Response(serializer.data)

   def  post(self, request):
        serializer = Doctor_detailSerializer(data=request.data)  

        if serializer.is_valid():
            serializer.save():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  


     
# Create your views here.

