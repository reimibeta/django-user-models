from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    """ Help Django work with our custom user model. """

    def create_user(self, name, password=None):
        """ Creates a new user object."""

        # if not email:
        #     raise ValueError('Users must have an email address.')

        # email = self.normalize_email(email)
        user = self.model(name=name, password=password)
        # user = self.model(email=email, name=name, raw_password=raw_password)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, password):
        """ Creates and saves a new superuser with given details."""

        user = self.create_user(name, password)
        # user.raw_password = raw_password
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    # raw_password = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'name'  # 'email' default

    # REQUIRED_FIELDS = ['name']

    # def get_full_name(self):
    #     """ Used to get a users short name. """
    #     return self.name

    # def get_short_name(self):
    #     """ Used to get a users short name. """
    #     return self.name

    def __str__(self):
        """ Django uses this when it needs to convert the object to a string """

        return self.name

    # def save(self, *args, **kwargs):
    #     super(User, self).save(*args, **kwargs)
