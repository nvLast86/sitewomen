from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError

from .models import Category, Husband


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label="Заголовок", min_length=5,
                            error_messages={
                                'min_length': 'Слишком короткое название',
                                'required': 'Без заголовка никак',
                            })
    slug = forms.SlugField(max_length=255, label="URL",
                           validators=[
                               MinLengthValidator(5, message='Минимум 5 символов'),
                               MaxLengthValidator(255, message='Максимум 255 символов'),
                           ])
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label='Контент')
    is_published = forms.BooleanField(required=False, initial=True, label='Статус')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана', label='Категории')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, empty_label='Не замужем', label='Муж')

    def clean_title(self):
        title = self.cleaned_data['title']
        ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмпнопрстуфхцчшщьыъэюя0123456789- "

        if not (set(title) <= set(ALLOWED_CHARS)):
            raise ValidationError("Должны присутствовать только русские символы, дефис и пробел")

