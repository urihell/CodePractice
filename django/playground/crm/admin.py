from django.contrib import admin

from .models import Organization, Customer, Job

admin.site.register(Organization)
admin.site.register(Customer)
admin.site.register(Job)

