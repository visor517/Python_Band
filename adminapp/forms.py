from django import forms
from authapp.models import HabrUser
from authapp.forms import UserEditForm
from articleapp.models import Category, Article

chek_list = ['is_active', 'is_delete', 'is_staff', 'is_deleted']


class UserRegisterForm(UserEditForm):
    class Meta:
        model = HabrUser
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name in chek_list:
                field.widget.attrs['class'] = 'form-chek'
                field.help_text = ''
                continue
            if field_name not in chek_list:
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''


class CategoryEditForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name in chek_list:
                field.widget.attrs['class'] = 'form-chek'
                field.help_text = ''
                continue
            if not field_name == 'is_delete':
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''


class ArticletEditForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not field_name == 'is_delete':
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''
