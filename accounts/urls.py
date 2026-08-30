from django.urls import path

from .views import LoginView, LogoutView, MeView, RegisterView


urlpatterns = [
    path(
        "register/",
        RegisterView.as_view(),
        name="register",
    ),

    path(
        "login/",
        LoginView.as_view(),
        name="login",
    ),

    path(
        "me/",
        MeView.as_view(),
        name="me",
    ),

    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
]