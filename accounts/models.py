import os
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


def path_and_rename(instance, filename):
    upload_to = 'user-uploads/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}-{}.{}'.format(instance.pk, instance.username, ext)
    return os.path.join(upload_to, filename)


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    # add additional fields in here
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="date joined", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    birth_date = models.DateField(null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    post_code = models.CharField(max_length=6)
    street = models.CharField(max_length=50)
    house_number = models.CharField(max_length=4)
    profile_picture = models.ImageField(upload_to=path_and_rename, null=True, blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
