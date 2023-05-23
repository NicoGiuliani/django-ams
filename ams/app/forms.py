from datetime import date
from django import forms
from django.db import models
from .models import Entry, FeedingSchedule, Note
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.forms.widgets import PasswordInput, TextInput, EmailInput


class CreateForm(forms.ModelForm):
    current_year = date.today().year
    year_range = [x for x in range(current_year - 20, current_year + 1)]

    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control rounded",
                "placeholder": "Name",
                "title": "Name",
            }
        ),
        label="",
    )
    common_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control rounded",
                "placeholder": "Common name",
                "title": "Common name",
            }
        ),
        label="",
    )
    species = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control rounded",
                "placeholder": "Species",
                "title": "Species",
            }
        ),
        label="",
    )
    sex = forms.ChoiceField(
        choices=(
            ("", "Sex"),
            ("MALE", "Male"),
            ("FEMALE", "Female"),
            ("UNKNOWN", "Unknown"),
        ),
        widget=forms.Select(attrs={"class": "form-control rounded", "title": "Sex"}),
        label="",
        required=True,
    )
    date_acquired = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "text",
                "class": "form-control rounded",
                "placeholder": "Date acquired",
                "onfocus": "(this.type='date')",
                "onblur": "if (this.value === '') { (this.type='text') }",
                "title": "Date acquired",
            }
        ),
        label="",
    )
    acquired_from = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control rounded",
                "placeholder": "Acquired from",
                "title": "Acquired from",
            }
        ),
        label="",
    )
    photo = forms.ImageField(
        widget=forms.FileInput(attrs={"class": "form-control rounded"}),
        label="",
        required=False,
    )

    class Meta:
        model = Entry
        fields = [
            "name",
            "common_name",
            "species",
            "date_acquired",
            "acquired_from",
            "photo",
            "sex",
        ]


class NoteForm(forms.ModelForm):
    text = forms.CharField(
        max_length=500,
        widget=forms.Textarea(
            attrs={
                "class": "form-control rounded",
                "placeholder": "Add a note",
                "title": "Note",
                "rows": 4,
            }
        ),
        label="",
    )

    class Meta:
        model = Note
        fields = ["text"]


class ScheduleForm(forms.ModelForm):
    current_year = date.today().year
    year_range = [x for x in range(current_year - 20, current_year + 1)]

    food_type = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control rounded",
                "placeholder": "Food type",
                "title": "Food Type",
            }
        ),
        label="",
        required=True,
    )
    food_quantity = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control rounded",
                "placeholder": "Food quantity",
                "title": "Food quantity",
            }
        ),
        label="",
        required=True,
    )
    last_fed_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "text",
                "class": "form-control rounded",
                "placeholder": "Last fed date",
                "onfocus": "(this.type='date')",
                "onblur": "if (this.value === '') { (this.type='text') }",
                "title": "Last fed date",
            }
        ),
        label="",
        required=True,
    )
    feed_interval = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control rounded",
                "placeholder": "Feed interval",
                "title": "Feed interval",
            }
        ),
        label="",
        required=True,
    )
    next_feed_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "text",
                "class": "form-control rounded",
                "placeholder": "Next feed date (optional)",
                "onfocus": "(this.type='date')",
                "onblur": "if (this.value === '') { (this.type='text') }",
                "title": "Next feed date",
            }
        ),
        label="",
        required=False,
    )

    class Meta:
        model = FeedingSchedule
        fields = [
            "food_type",
            "food_quantity",
            "last_fed_date",
            "feed_interval",
            "next_feed_date",
        ]


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        widget=TextInput(
            attrs={
                "class": "form-control rounded",
                "placeholder": "Username",
            }
        )
    )
    password = forms.CharField(
        widget=PasswordInput(
            attrs={"class": "form-control rounded", "placeholder": "Password"}
        )
    )


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label="",
        max_length=50,
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Username",
            }
        ),
    )
    email = forms.EmailField(
        widget=EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email",
            }
        )
    )
    password1 = forms.CharField(
        label="",
        widget=PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
    )
    password2 = forms.CharField(
        label="",
        widget=PasswordInput(
            attrs={"class": "form-control", "placeholder": "Repeat password"}
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)
        print("password reset form")

    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control rounded",
                "placeholder": "Email",
                "type": "email",
                "name": "email",
            }
        ),
    )


class UserSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(UserSetPasswordForm, self).__init__(*args, **kwargs)
        print("new password form")

    new_password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control rounded",
                "placeholder": "New password",
                "type": "password",
                "name": "password1",
            }
        ),
    )

    new_password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "New password confirmation",
                "type": "password",
                "name": "password2",
            }
        ),
    )
