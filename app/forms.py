"""
Definition of forms.
"""

from cProfile import label
from calendar import c
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

from django.db import models
from .models import Comment, Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))
    
class AnketaForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
    gender = forms.ChoiceField(label='Ваш пол',
        choices=[('1', 'Мужской'), ('2', 'Женский')],
        widget=forms.RadioSelect, initial=1)
    like = forms.CharField(label=' Что вам понравилось на сайте',
        widget=forms.Textarea(attrs={'rows':7,'cols':30}))
    dislike = forms.CharField(label='Что вам не понравилось на сайте?  Какие были сложности или недочеты',
        widget=forms.Textarea(attrs={'rows':7,'cols':30}))
    internet = forms.ChoiceField(label='Ваша общая оценка сайта',
        choices=(('1', 'Крайне негативная'),
            ('2', 'Нейтральная'),
            ('3', 'Удовлетворительная'),
            ('4', 'Хорошая'),
            ('5', 'Отличная')), initial=1)

    notice = forms.BooleanField(label='Получать новости об обновлениях сайта на e-mail?', required=False)
    email = forms.EmailField(label='Ваш e-mail', min_length=7)
    message = forms.CharField(label='Ваши предложения и пожелания по улучшению сайта',
        widget=forms.Textarea(attrs={'rows':7,'cols':30}))

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка" }
    