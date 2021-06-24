from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.shortcuts import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Article(models.Model):
    title = models.CharField(max_length=255)
    # image = models.ImageField()
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ['date_created']

    # def __str__(self):
    #     return "{} by {}".format(self.title,)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('article-detail', args=[str(self.id)])


class Comment(models.Model):
    pass
from django.db import models

# Create your models here.
