from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import CustomUser

# Create your models here.
User = get_user_model()

class UserProfile(models.Model):
    username = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    friends = models.ManyToManyField('self',blank=True)
    
    def __str__(self):
        return str(self.username)

class UserPost(models.Model):
    username = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    post = models.TextField(max_length=1024)
    postpic = models.FileField(null=True,blank=True)
    postdate = models.DateTimeField(auto_now_add=True)
    postlike = models.ManyToManyField(User, related_name='postlikes')

class UserPostComment(models.Model):
    postid = models.ForeignKey(
        UserPost,
        on_delete=models.CASCADE,
    )
    username = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    comment = models.TextField(max_length=1024)
    commentpic = models.FileField(null=True,blank=True)
    commentdate = models.DateTimeField(auto_now_add=True)

class SitePost(models.Model):
    username = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    post = models.TextField(max_length=1024)
    postpic = models.FileField(null=True,blank=True)
    postdate = models.DateTimeField(auto_now_add=True)

class SiteSetting(models.Model):
    # This is a name value pair of various settings
    # for the site.
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)