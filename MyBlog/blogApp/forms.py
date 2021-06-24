from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from . models import Article
from django.contrib.auth.models import User


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        # fields = '__all__'
        exclude = ('author',)


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
