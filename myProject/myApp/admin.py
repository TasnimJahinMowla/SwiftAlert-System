from django.contrib import admin
from .models import *

admin.site.register(Location)
admin.site.register(CrimeType)
admin.site.register(IncidentReport)
admin.site.register(Notification)
admin.site.register(UserProfile)
