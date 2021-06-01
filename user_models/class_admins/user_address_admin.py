from django.contrib import admin

from user_models.class_models.user_address import UserAddress


class UserAddressInline(admin.TabularInline):
    model = UserAddress
    extra = 0
