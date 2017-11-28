from django.db import models
from django.utils import timezone
from userauth.models import MyUser as User

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    @property
    def likes(self):
         return Like.objects.filter(post=self).count()


    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)

class Comment(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
