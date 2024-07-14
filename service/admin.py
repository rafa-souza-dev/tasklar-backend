from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'consumer', 'job', 'tasker', 'request_description', 'date', 'status', 'value', 'uf', 'city', 'neighborhood')

    def user(self, obj):
        return obj.consumer.user.email if obj.consumer else '-'
    user.short_description = 'User Email'
