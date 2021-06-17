from rest_framework import viewsets, status
from rest_framework.response import Response

from user_models.class_models.user_phone import UserPhone
from user_models.class_serializers.user_phone_serializers import UserPhoneSerializer
from django_rest_framework.pagination import StandardResultsSetPagination


class UserPhoneNumberViewSet(viewsets.ModelViewSet):
    queryset = UserPhone.objects.all()
    serializer_class = UserPhoneSerializer
    pagination_class = StandardResultsSetPagination

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
