from django.contrib import admin
from .models import Visit, Company, Team

# Register your models here.
admin.site.register(Visit)
admin.site.register(Team)
admin.site.register(Company)