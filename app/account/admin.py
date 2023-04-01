from django.contrib import admin

from .models import Address, User


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']
admin.site.register(User, UserAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ['address', 'city', 'postcode']
admin.site.register(Address, AddressAdmin)
