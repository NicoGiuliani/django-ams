from django.conf import settings
from django.urls import path, include, re_path
from . import views
from .forms import UserLoginForm, UserSetPasswordForm, UserPasswordResetForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("entry/<uuid:id>/", views.entry, name="entry"),
    path("notes/<uuid:id>/", views.notes, name="notes"),
    path("edit_note/<uuid:id>/", views.edit_note, name="edit_note"),
    path("delete_note/<uuid:id>/", views.delete_note, name="delete_note"),
    path("create/", views.create, name="create"),
    path("register/", views.register, name="register"),
    path("edit/<uuid:id>/", views.edit, name="edit"),
    path("delete/<uuid:id>/", views.delete, name="delete"),
    path("delete_photo/<uuid:id>/", views.delete_photo, name="delete_photo"),
    path("schedule/<uuid:id>/", views.schedule, name="schedule"),
    path("delete_schedule/<uuid:id>/", views.delete_schedule, name="delete_schedule"),
    path("search/", views.search, name="search"),
    path(
        "accounts/reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_confirm.html",
            form_class=UserSetPasswordForm,
        ),
        name="password_reset_confirm",
    ),
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=UserLoginForm,
        ),
        name="login",
    ),
    path(
        "accounts/logout/",
        views.custom_logout,
        name="logout",
    ),
    path(
        "accounts/password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="registration/password_reset_form.html",
            form_class=UserPasswordResetForm,
        ),
        name="password_reset",
    ),
    path("accounts/", include("django.contrib.auth.urls")),
]
