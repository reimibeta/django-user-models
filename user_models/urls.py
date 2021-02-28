from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from . import views

from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

router = routers.DefaultRouter()
router.register('user', views.UserViewSet)
router.register('user_photo', views.UserPhotoViewSet)
router.register('user_phone', views.UserPhoneNumberViewSet)
router.register('user_address', views.UserAddressViewSet)

# Token
urlpatterns = [
    url(r'', include(router.urls)),
    path('user_token/', views.UserTokenObtainPairView.as_view()),
    path('user_token_refresh/', TokenRefreshView.as_view()),
    path('user_token_verify/', TokenVerifyView.as_view()),
]
