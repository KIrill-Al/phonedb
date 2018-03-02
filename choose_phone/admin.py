from django.contrib import admin
from .models import PhoneNumbersFile, Phone


admin.site.register(Phone)
admin.site.register(PhoneNumbersFile)
