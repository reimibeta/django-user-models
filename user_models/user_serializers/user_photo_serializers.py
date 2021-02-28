from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from .user_serializers import UserSerializer
from image_utils.base64_image_field import Base64ImageField
from ..models import UserPhoto


class UserPhotoSerializer(FlexFieldsModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True)

    photo = Base64ImageField(
        max_length=None, use_url=True,
    )

    class Meta:
        model = UserPhoto
        fields = ('id', 'url', 'user', 'photo', 'thumbnail')
        expandable_fields = {'user': UserSerializer}
