from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from htapp.models import AppUser, Person , Hospital,  Appointment,  Doctor_detail, Pharmacy, Fees, Invoice, Fees_type, Insurance, Laboratory, Feed_back, Result_test, Health_test

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'        


class Doctor_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor_detail
        fields = '__all__'

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'

class FeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fees
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


class Fees_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fees_type
        fields = '__all__'
 
class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'

class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = '__all__'   

class Feed_backSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed_back
        fields = '__all__'            

class Result_testSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result_test
        fields = '__all__'   

class Health_testSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health_test
        fields = '__all__'                         