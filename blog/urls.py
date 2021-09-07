"""blog URL Configuration..

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from account.views import Logout
# from post.views import DetailPostAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    # browser login
    path("api-auth/", include("rest_framework.urls")),

    # api authentication and token generation
    path("user/", include("account.urls", namespace="accounts")),

    # api
    path("posts/", include("post.urls", namespace="posts_api")),

    path('token/', obtain_auth_token, name='api_token_auth'),
    path('logout/', Logout.as_view(), name="logout"),
    # path("", DetailPostAPIView.as_view(), name="post-detail"),
]
