from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from .user_serializers import UserSerializer
from ..class_models.user import User
from ..class_models.user_address import UserAddress


class UserAddressSerializer(FlexFieldsModelSerializer):
    user_info = serializers.SerializerMethodField('user_info_field')

    def user_info_field(self, obj):
        items = User.objects.filter(id=obj.user.id)
        serializer = UserSerializer(items, read_only=True, many=True, context={'request': None})
        return serializer.data

    class Meta:
        model = UserAddress
        fields = ('id', 'url', 'user', 'user_info', 'address', 'map', 'city', 'country')
        expandable_fields = {'user': UserSerializer}
