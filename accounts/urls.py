
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import AuthRegister, RegisterAPIView, UserDetailAPIView, HelloAPIView, HelloViewSets

# viewset import
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', HelloViewSets,basename='hello-viewset')

urlpatterns = [
    path('token/', obtain_jwt_token),
    path('token/refresh/', refresh_jwt_token),
    path('token/verify/', verify_jwt_token),
    path('register/', RegisterAPIView.as_view()),
    path('users/<str:username>/', UserDetailAPIView.as_view()),
    path('testing/hello/', HelloAPIView.as_view()),
    path('', include(router.urls))
]
