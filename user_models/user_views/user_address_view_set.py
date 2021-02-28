from rest_framework import viewsets

from ..user_models.user_address import UserAddress
from ..user_serializers.user_address_serializers import UserAddressSerializer
from rest_framework_utils.pagination import StandardResultsSetPagination

class UserAddressViewSet(viewsets.ModelViewSet):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    pagination_class = StandardResultsSetPagination
