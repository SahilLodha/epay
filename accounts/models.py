from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import EmailValidator
from django.db import models


# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('Email Address is a Required Field.')

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(email=self.normalize_email(email), password=password,
                                first_name=first_name, last_name=last_name)
        user.is_vendor = False
        user.is_active = True
        user.is_staff = False
        user.is_customer = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_vendor(self, first_name, last_name, email, password):
        user = self.create_user(email=self.normalize_email(email), password=password,
                                first_name=first_name, last_name=last_name)
        user.is_vendor = True
        user.is_active = True
        user.is_customer = False
        user.is_superuser = False
        user.is_staff = False
        user.save(using=self._db)

    def create_customer(self, first_name, last_name, email, password=None):
        user = self.create_user(email=email, password=password,
                                first_name=first_name, last_name=last_name)
        user.is_vendor = False
        user.is_active = True
        user.is_customer = True
        user.is_superuser = False
        user.is_staff = False
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True, validators=[EmailValidator])
    phone_no = models.CharField(max_length=50, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_customer = models.BooleanField(default=True)
    is_vendor = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # Django Defaults
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name(self):
        return self.first_name.capitalize() + ' ' + self.last_name.capitalize()

    class Meta:
        db_table = 'accounts'

