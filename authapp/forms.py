from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import fields
from .models import HabrUser, HabrProfile

from django.contrib.auth.forms import UserChangeForm

import random
import hashlib



class UserLoginForm(AuthenticationForm):
    class Meta:
        model = HabrUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = HabrUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1',
                  'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def save(self):
        user = super().save()

        user.is_active = False
        salt = hashlib.sha1(
            str(random.random()).encode('utf8')).hexdigest()[:6]

        user.activation_key = hashlib.sha1(
            (user.email + salt).encode('utf8')).hexdigest()
        user.save()

        return user


class UserEditForm(UserChangeForm):
    class Meta:
        model = HabrUser
        # fields = ('username', 'first_name', 'password1',
        #           'password2', 'email', 'birthday', 'avatar')
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = HabrProfile
        # fields = ('tagline', 'about_me', 'gender', 'avatar', 'url')
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'avatar':
                field.widget = forms.HiddenInput()
