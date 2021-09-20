from django.urls import path, include
from .views import UserCreateAPIView, UserListAPIView, UserDetailAPIView


app_name = "accounts"

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_detail"),
    # path('token/', obtain_auth_token, name='api_token_auth'),
    path("register/", UserCreateAPIView.as_view(), name="user_create"),
    path("<int:id>/", UserDetailAPIView.as_view(), name="user_detail"),
]
