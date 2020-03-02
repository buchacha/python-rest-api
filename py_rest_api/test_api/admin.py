from django.contrib import admin
from .models import Employee, HR, Employer

# Register your models here.

admin.site.register(Employee)
admin.site.register(HR)
admin.site.register(Employer)

