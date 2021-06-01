from django.contrib.auth.handlers.modwsgi import check_password
from django.contrib.auth.hashers import make_password
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from user_models.class_models.user import User


class UserSerializer(FlexFieldsModelSerializer):
    def validate(self, attrs):
        data = super(UserSerializer, self).validate(attrs)
        user_queryset = User.objects.filter(name=attrs['name']).first()
        if user_queryset and attrs['password'] is None or attrs['raw_password'] is None or attrs['password'] == '' or \
                attrs['raw_password'] == '':
            attrs['password'] = user_queryset.password
            attrs['raw_password'] = user_queryset.raw_password
        else:
            # need to use re-enter password and confirm password
            # print(attrs['raw_password'])
            hashed_pwd = make_password(attrs['password'])
            # print(hashed_pwd)
            # print(attrs['password'])
            # check_password(attrs['password'], hashed_pwd)  # returns True
            attrs['password'] = hashed_pwd
        return data

    # product = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'url',
            'email',
            'name',
            'first_name', 'last_name',
            'password', 'raw_password'
        )
        # validators = []
        extra_kwargs = {
            'password': {'write_only': True},
            'raw_password': {'write_only': True}
        }
