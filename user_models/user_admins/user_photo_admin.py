from django.contrib import admin

from ..user_models.user_photo import UserPhoto


class UserPhotoAdminInline(admin.TabularInline):
    model = UserPhoto
    extra = 0
