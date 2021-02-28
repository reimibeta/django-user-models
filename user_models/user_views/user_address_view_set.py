from rest_framework import viewsets

from ..user_models.user_address import UserAddress
from ..user_serializers.user_address_serializers import UserAddressSerializer
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 200
    page_size_query_param = 'page_size'

class UserAddressViewSet(viewsets.ModelViewSet):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    pagination_class = StandardResultsSetPagination
