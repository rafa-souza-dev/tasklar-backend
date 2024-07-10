from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from localflavor.br import models as local_flavor_models
from django.db import models
from django.core.validators import RegexValidator


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    class ProfileType(models.TextChoices):
        TASKER = 'T', 'Tasker'
        CONSUMER = 'C', 'Consumer'

    phone_validator = RegexValidator(
        regex=r'^\(\d{2}\) \d{4,5}-\d{4}$',
    )

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    uf = local_flavor_models.BRStateField()
    city = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, validators=[phone_validator])
    profile_type = models.CharField(max_length=1, choices=ProfileType.choices, default=ProfileType.CONSUMER)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
