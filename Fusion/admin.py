from django.contrib import admin
from Fusion.models import *

@admin.register(VendorRegistraion)
class VendorRegistrationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in VendorRegistraion._meta.get_fields()]

@admin.register(SmallBusinessRegistration)
class SmallBusinessRegistrationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SmallBusinessRegistration._meta.get_fields()]

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Vendor._meta.get_fields()]

