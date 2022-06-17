from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from . import forms

USER_MODEL = get_user_model()


@admin.register(USER_MODEL)
class UserAdmin(UserAdmin):
    model = USER_MODEL
    ordering = ('email', )

    add_form = forms.UserCreationForm
    form = forms.ChangeUserForm

    list_display = ('id', 'email', 'is_staff', 'is_active', )
    list_display_links = ('id', 'email', )

    fieldsets = (
        (None, {'fields': ('email', )}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', )}),
    )