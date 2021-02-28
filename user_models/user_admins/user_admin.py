from django.contrib import admin

from ..user_admins.user_address_admin import UserAddressInline
from ..user_admins.user_phone_admin import UserPhoneNumberInline
from ..user_admins.user_photo_admin import UserPhotoAdminInline
from ..user_models.user import User
from ..user_models.user_phone import UserPhone
from ..user_models.user_photo import UserPhoto
from ..render_image import RenderImage


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'email', 'phone_number', 'is_staff', 'is_superuser')

    # readonly_fields = ('password',)

    def image(self, obj):
        image = UserPhoto.objects.filter(user=obj.id).first()
        if image:
            return RenderImage.renderHtmlImage(image.thumbnail.url)
        else:
            return 'image not provided'

    def phone_number(self, data):
        phones = UserPhone.objects.filter(user=data.id)
        data = []
        for phone in phones:
            data.append(phone.phone)
        return ", ".join(data)

    def save_model(self, request, obj, form, change):
        if not change:
            # obj.raw_password = obj.password
            obj.set_password(obj.raw_password)
        obj.save()

    def save_related(self, request, form, formsets, change):
        super(UserAdmin, self).save_related(request, form, formsets, change)
        user = form.instance
        # if not change:
        check_password = user.check_password(user.raw_password)
        if not check_password:
            # user.raw_password = user.password
            user.set_password(user.raw_password)
            user.save()
            print(check_password)

    inlines = [
        UserPhotoAdminInline,
        UserAddressInline,
        UserPhoneNumberInline,
    ]


admin.site.register(User, UserAdmin)
