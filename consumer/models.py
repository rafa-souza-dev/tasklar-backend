from django.db import models

from authentication.models import User


class Consumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True, blank=True, default=None)

    def __str__(self):
        return self.user.email
