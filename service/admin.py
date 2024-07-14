from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'job', 'tasker', 'status', 'date', 'value', 'uf', 'city', 'neighborhood')
    readonly_fields = ('id',)
