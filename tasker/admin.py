from django.contrib import admin

from tasker import models

admin.site.register(models.Tasker)
admin.site.register(models.Period)
admin.site.register(models.Category)
