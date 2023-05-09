from django.contrib import admin

from accounts.views import hotel_owner_home
from .models import *
# Register your models here.

from django.contrib import admin
from .models import NormalUser

class NormalUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'lastname', 'phone_num', 'email', 'last_login')  # fields to be displayed in table
    
    # def get_user_id(self, obj):
    #     return f'US{obj.id:04d}'
    # get_user_id.short_description = 'User ID'

admin.site.register(NormalUser, NormalUserAdmin)

class HotelAdmin(admin.ModelAdmin):
    list_display = ('ho_id', 'username', 'lastname', 'email', 'last_login')

admin.site.register(HotelOwner, HotelAdmin)

admin.site.register(CabDriver)
admin.site.register(appartment_booking)
admin.site.register(appartment_bookings)
admin.site.register(Appartment)
