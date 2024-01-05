
# Register your models here.
from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','username', 'password', 'email','phone_number')  # Customize the fields you want to display
    # Add other configurations as needed





