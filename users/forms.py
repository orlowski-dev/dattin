from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()


class CreateUserForm(UserCreationForm):
    class Meta:
        model = USER_MODEL
        fields = ('email', )


class ChangeUserForm(UserChangeForm):
    class Meta:
        model = USER_MODEL
        fields = ('email', )