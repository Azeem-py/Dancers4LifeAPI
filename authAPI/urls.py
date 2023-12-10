from knox import views as knox_views
from .views import *
from django.urls import path, include

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"signup", SignUpView, basename="signup")
# router.register(r'user-info', UserInfoView, basename='user-info')

urlpatterns = [
    path(r'login/', LoginView.as_view(), name='knox_login'),
    path(r'logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path(r'logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path("", include(router.urls)),
    path("get-otp/<int:id>", SignUpView.as_view({"get": "otp"})),
    path("get-otp/password/<str:email>", SignUpView.as_view({"get": "otp"})),
    path("getID/", GetID.as_view({"get": "getID"})),
    path("is-auth/", checkAuth.as_view({"get": "isAuth"})),
]