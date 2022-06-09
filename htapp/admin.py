from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import AppUser, Person, Test 
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
admin.site.register(Test)



