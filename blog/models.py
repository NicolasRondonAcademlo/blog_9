from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    title = models.CharField(max_length=250)
    text = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    date_last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
