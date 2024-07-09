from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'contact', 'value', 'duration', 'start_time', 'end_time', 'display_days_of_week')
    list_filter = ('category', 'duration')
    search_fields = ('category__name', 'contact')

    def display_days_of_week(self, obj):
        return obj.days_of_week
    display_days_of_week.short_description = 'Days of Week'
