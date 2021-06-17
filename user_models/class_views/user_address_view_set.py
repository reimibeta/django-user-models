from rest_framework import viewsets

from user_models.class_models.user_address import UserAddress
from user_models.class_serializers.user_address_serializers import UserAddressSerializer
from django_rest_framework.pagination import StandardResultsSetPagination


class UserAddressViewSet(viewsets.ModelViewSet):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    pagination_class = StandardResultsSetPagination
