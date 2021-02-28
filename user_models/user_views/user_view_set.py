from rest_framework import viewsets, status
from rest_framework.response import Response

from ..user_models.user import User
from ..user_serializers.user_serializers import UserSerializer
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 200
    page_size_query_param = 'page_size'


class UserViewSet(viewsets.ModelViewSet):
    """ Handles creating, creating and updating users. """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = StandardResultsSetPagination

    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('name', 'email',)
    # uncomment it when run production.
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # authentication_classes = [JWTAuthentication, ]

    def create(self, request, **kwargs):
        # obj = lambda: None
        # Set your serializer
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():  # MAGIC HAPPENS HERE
            # ... Here you do the routine you do when the data is valid
            # You can use the serializer as an object of you Assets Model
            # Save it
            serializer.save()
            serializer_dict = serializer.data
            serializer_dict['success'] = True
            return Response(serializer_dict, status=status.HTTP_201_CREATED)
        else:
            # request.data['email'].error_messages['required'] = u'My custom required msg'
            serializer_dict = serializer.errors
            serializer_dict['success'] = False
            return Response(serializer_dict, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, project_pk=None):
        instance = self.queryset.get(pk=pk)
        serializer = self.serializer_class(instance, data=request.data, partial=True, context={'request': request})
        # serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            serializer_dict = serializer.data
            serializer_dict['success'] = True
            return Response(serializer_dict)
        else:
            serializer_dict = serializer.errors
            serializer_dict['success'] = False
            return Response(serializer_dict)

    def get_queryset(self):
        qs = super().get_queryset()
        # print('Category: {}'.format(self.request.GET['category']))
        if 'email' in self.request.GET:
            request = self.request.GET['email']
            # print(request)
            user = User.objects.filter(email=request).first()
            if user:
                # return User.objects.filter(department=type.department)
                return User.objects.filter(id=user.id)
            else:
                return []
        else:
            return qs
