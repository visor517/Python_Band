from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from authapp.models import HabrUser, HabrProfile
from authapp.forms import UserEditForm, UserProfileEditForm
from articleapp.models import Category, Article

CHECK_LIST = ['is_active', 'is_delete', 'is_staff', 'is_deleted']


def add_class_html(fields):
    for field_name, field in fields.items():
        if field_name in CHECK_LIST:
            field.widget.attrs['class'] = 'form-chek'
            field.help_text = ''
            continue
        else:
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class UserUpdateForm(UserEditForm):
    class Meta:
        model = HabrUser
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active', 'role', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_class_html(self.fields)


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = HabrUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1',
                  'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_class_html(self.fields)


class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = HabrProfile
        fields = ('tagline', 'gender', 'birthday', 'zone')
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_class_html(self.fields)


class CategoryRegisterForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_class_html(self.fields)


class ArticleRegisterForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_class_html(self.fields)
