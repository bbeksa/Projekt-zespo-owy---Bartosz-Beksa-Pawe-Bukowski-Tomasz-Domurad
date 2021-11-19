from django.contrib import admin
from .models import *

admin.site.register(City)
admin.site.register(Address)
admin.site.register(Personal_Data)
admin.site.register(Service)
admin.site.register(Invoice)
admin.site.register(Service_Invoice)


