from rest_framework import viewsets

from user_models.class_models.user_photo import UserPhoto
from user_models.class_serializers.user_photo_serializers import UserPhotoSerializer
from rest_framework_utils.pagination import StandardResultsSetPagination


class UserPhotoViewSet(viewsets.ModelViewSet):
    queryset = UserPhoto.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = UserPhotoSerializer
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('user',)
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)  # IsAuthenticated
    # authentication_classes = [JWTAuthentication, ]
