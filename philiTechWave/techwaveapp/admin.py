# techwaveapp/admin.py

from django.contrib import admin
from .models import Customer, TechSupportService, CybercafeUsage, TrainingProgram, ContactMessage, Ticket

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Customer)
admin.site.register(TechSupportService)
admin.site.register(CybercafeUsage)
admin.site.register(TrainingProgram)
admin.site.register(ContactMessage)
admin.site.register(Ticket)

