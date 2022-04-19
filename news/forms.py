from .models import News
from django.forms import ModelForm, TextInput, Textarea, ImageField


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['author','title', 'anons', 'full_text', 'image']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placerholder': 'Название статьи'
            }),
            'anons': Textarea(attrs={
                'class': 'form-control',
                'placerholder': 'Анонс'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placerholder': 'Текст статьи'
            }),
        }
