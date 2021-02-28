from django.db import models

from .user import User


class UserPhone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    region = models.CharField(max_length=10, blank=True, null=True)
    country_code = models.CharField(max_length=100, blank=True, null=True)
    national = models.CharField(max_length=100, blank=True, null=True)
    national_number = models.CharField(max_length=100, blank=True, null=True)
    international = models.CharField(max_length=100, blank=True, null=True)
    international_standard = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, unique=True)

    class Meta:
        unique_together = (('user', 'phone'),)

    def __str__(self):
        return '{}({})'.format(self.user, self.phone)
