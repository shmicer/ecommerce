from django.contrib import admin

from .models import Address, User


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'current_address', 'current_pickpoint']
admin.site.register(User, UserAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ['address', 'city', 'postcode']
admin.site.register(Address, AddressAdmin)
