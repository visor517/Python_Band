from django.forms import ModelForm

from articleapp.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'category', 'content', 'image')

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
