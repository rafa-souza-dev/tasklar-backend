from django.db import models

from authentication.models import User


class Period(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tasker(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    periods = models.ManyToManyField(Period)
    phone = models.CharField(max_length=255)
    hourly_rate = models.DecimalField(max_digits=11, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.user.email
