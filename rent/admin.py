from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Car)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Extended_order)