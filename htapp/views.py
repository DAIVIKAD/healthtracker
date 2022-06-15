from django.shortcuts import render
from rest_framework import Permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIview
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_password
from .models import  Person , Hospital,  Appointment,  Doctor_detail, Pharmacy, Fees, Invoice, Fees_type, Insurance, Laboratory, Feed_back, Result_test, Health_test
from .serializers import Personserializers , Hospitalserializers,  Appointmentserializers,  Doctor_detailserializers, Pharmacyserializers, Feesserializers, Invoiceserializers, Fees_typeserializers, Insuranceserializers, Laboratoryserializers, Feed_backserializers, Result_testserializers, Health_testserializers



# Create your views here.

