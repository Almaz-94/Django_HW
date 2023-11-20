from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email','password1', 'password2')


class UserLoginForm(StyleFormMixin, AuthenticationForm):

    class Meta:
        model = User
        fields = ('email','password',)


class UserForm(StyleFormMixin, UserChangeForm):

    class Meta:
        model = User
        fields = ('phone', 'avatar', 'country', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()


class ManagerBansUserForm(StyleFormMixin, UserChangeForm):

    class Meta:
        model = User
        fields = ('is_active', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
