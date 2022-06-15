from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import AppUser, Person , Hospital,  Appointment,  Doctor_detail, Pharmacy, Fees, Invoice, Fees_type, Insurance,Laboratory, Feed_back, Result_test, Health_test

from django.contrib.auth.admin  import UserAdmin

# Register your models here.

class UserAdminConfig(UserAdmin):
    search_fields =('email', 'first_name', 'branch_code','staff_id',)
    list_filter = ('email', 'first_name', 'branch_code','staff_id','is_active', 'is_staff',)
    ordering =('-start_date',)
    list_display = ('email', 'first_name', 'last_name', 'branch_code','staff_id', 'is_active', 'is_staff')
    fieldsets = (
        ('User Details', {'fields':('email', 'first_name', 'last_name')}),
        ('Permissions', {'fields':('is_staff', 'is_active')}),
        ('Others', {'fields':('start_date',)}),
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','first_name', 'last_name', 'branch_code','staff_id', 'is_active', 'is_staff',),
        }),
    )
   

admin.site.register(AppUser, UserAdminConfig)
admin.site.register(Person)
admin.site.register(Appointment)
admin.site.register(Hospital)
admin.site.register(Doctor_detail)
admin.site.register(Pharmacy)
admin.site.register(Fees)
admin.site.register(Invoice)
admin.site.register(Fees_type)
admin.site.register(Insurance)
admin.site.register(Laboratory)
admin.site.register(Feed_back)
admin.site.register(Result_test)
admin.site.register(Health_test)





