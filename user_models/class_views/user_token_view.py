from django.core import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from user_models.class_models.user import User


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': {
            "message": "Email and password not found.",
            "success": False,
        },
    }

    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(UserTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        # data.update({'user': self.user.username})
        # data.update({'id': self.user.id})
        # and everything else you want to send in the response
        # user_queryset = User.objects.filter(email=attrs['email']).first()
        user_queryset = User.objects.first()

        user = {
            "id": user_queryset.id,
            "username": user_queryset.name,
            "email": user_queryset.email,
            # "photo": HOST_URL + user_photo_queryset.photo.url
        }
        # user = {}
        return {
            "token": data,
            "user": user,
            "success": True
        }
        # serializers.serialize("user", user)


class UserTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = UserTokenObtainPairSerializer
    # serializer_class.errors = {"data": "test"}
    # print("tst")
    # def create(self, request, **kwargs):
    #     # obj = lambda: None
    #     # Set your serializer
    #     serializer = self.serializer_class(data=request.data, context={'request': request})
    #     if serializer.is_valid():  # MAGIC HAPPENS HERE
    #         # ... Here you do the routine you do when the data is valid
    #         # You can use the serializer as an object of you Assets Model
    #         # Save it
    #         serializer.save()
    #         serializer_dict = serializer.data
    #         serializer_dict['success'] = True
    #         return Response(serializer_dict, status=status.HTTP_201_CREATED)
    #     else:
    #         # request.data['email'].error_messages['required'] = u'My custom required msg'
    #         serializer_dict = serializer.errors
    #         serializer_dict['success'] = False
    #         return Response(serializer_dict, status=status.HTTP_400_BAD_REQUEST)
    #
    # def update(self, request, pk=None, project_pk=None):
    #     instance = self.queryset.get(pk=pk)
    #     serializer = self.serializer_class(instance, data=request.data, partial=True, context={'request': request})
    #     # serializer.is_valid(raise_exception=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         serializer_dict = serializer.data
    #         serializer_dict['success'] = True
    #         return Response(serializer_dict)
    #     else:
    #         serializer_dict = serializer.errors
    #         serializer_dict['success'] = False
    #         return Response(serializer_dict)
