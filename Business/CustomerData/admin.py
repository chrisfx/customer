from django.contrib import admin

# Register your models here.

from CustomerData.models import Customer

#admin.site.register(Customer)
# Define the admin class
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'street_name', 'city', 'state', 'Zip')
    fields = [('last_name', 'first_name'), 'street_name', ('city', 'state', 'Zip')]

# Register the admin class with the associated model
#admin.site.register(Customer, CustomerAdmin)

