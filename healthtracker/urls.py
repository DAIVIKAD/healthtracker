"""healthtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.urls import re_path as url
from htapp import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers, serializers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    url(r'^api/person/', views.API_Person.as_view()),
    url(r'^api/hospital/', views.API_Hospital.as_view()),
    url(r'^api/appointment/', views.API_Appointment.as_view()),
    url(r'^api/doctor_detail/', views.API_Doctor_detail.as_view()),
    url(r'^api/pharmacy/', views.API_Pharmacy.as_view()),
    url(r'^api/fees/', views.API_Fees.as_view()),
    url(r'^api/invoice/', views.API_Invoice.as_view()),
    url(r'^api/fees_type/', views.API_Fees_type.as_view()),
    url(r'^api/insurance/', views.API_Insurance.as_view()),
    url(r'^api/laboratory/', views.API_Laboratory.as_view()),
    url(r'^api/feed_back/', views.API_Feed_back.as_view()),
    url(r'^api/result_test/', views.API_Result_test.as_view()),
    url(r'^api/health_test/', views.API_Health_test.as_view()),
    path('Person/<int:pk',views.Person_detail),
    path('Hospital/<int:pk',views.Hospital_detail),
    path('Appointment/<int:pk',views.Appointment_detail),
    path('Person/<int:pk',views.Person_detail),
    path('Person/<int:pk',views.Person_detail),
    
]
