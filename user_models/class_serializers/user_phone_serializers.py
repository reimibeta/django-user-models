from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from .user_serializers import UserSerializer
from ..class_models.user import User
from ..class_models.user_phone import UserPhone


class UserPhoneSerializer(FlexFieldsModelSerializer):
    user_info = serializers.SerializerMethodField('user_info_field')

    def user_info_field(self, obj):
        items = User.objects.filter(id=obj.user.id)
        serializer = UserSerializer(items, read_only=True, many=True, context={'request': None})
        return serializer.data

    class Meta:
        model = UserPhone
        fields = (
            'id', 'url', 'user', 'user_info', 'region', 'country_code', 'national', 'national_number', 'international',
            'international_standard',
            'phone', 'type')
        expandable_fields = {'user': UserSerializer}
