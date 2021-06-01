from django.contrib import admin

from user_models.class_models.user_phone import UserPhone


class UserPhoneNumberInline(admin.TabularInline):
    model = UserPhone
    extra = 0
