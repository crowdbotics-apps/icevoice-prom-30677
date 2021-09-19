from django.contrib import admin
from .models import VerificationCode, Profile, Contact

admin.site.register(VerificationCode)
admin.site.register(Profile)
admin.site.register(Contact)

# Register your models here.
