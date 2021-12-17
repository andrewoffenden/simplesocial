from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from accounts.models import CustomUser

# Create your models here.
User = get_user_model()

def post_upload_dir(instance, filename):
    return 'user_{0}/post_{1}/{2}'.format(instance.username, instance.id, filename)

def user_comment_upload_dir(instance, filename):
    return 'user_{0}/comment_{1}/{2}'.format(instance.username, instance.id, filename)

def group_post_upload_dir(instance, filename):
    return 'user_{0}/group_post_{1}/{2}'.format(instance.username, instance.id, filename)

def group_comment_upload_dir(instance, filename):
    return 'user_{0}/group_comment_{1}/{2}'.format(instance.username, instance.id, filename)

def site_post_upload_dir(instance, filename):
    return 'site_post_pics/site_post_{0}/user_{1}/{2}'.format(instance.id,instance.username, filename)

def navbar_icon_upload_dir(instance, filename):
    return 'navbar/{0}/{1}'.format(instance.name, filename)

def userprofile_avatar_upload_dir(instance, filename):
    return 'avatars/{0}/{1}'.format(instance.username, filename)

class UserProfile(models.Model):
    username = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    avatar = models.ImageField(upload_to=userprofile_avatar_upload_dir, null=True, blank=True)
    friends = models.ManyToManyField('self',blank=True, related_name='myfriends')
    
    def __str__(self):
        return str(self.username)


class UserPost(models.Model):
    username = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
    )
    post = models.TextField(max_length=1024)
    postpic = models.ImageField(upload_to=post_upload_dir, null=True, blank=True)
    postdate = models.DateTimeField(auto_now_add=True)
    postlike = models.ManyToManyField(User, related_name='user_postlikes', blank=True)

class UserPostComment(models.Model):
    postid = models.ForeignKey(
        UserPost,
        on_delete=models.CASCADE,
    )
    username = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
    )
    comment = models.TextField(max_length=1024)
    commentpic = models.ImageField(upload_to=user_comment_upload_dir, null=True,blank=True)
    commentdate = models.DateTimeField(auto_now_add=True)
    commentlike = models.ManyToManyField(User, related_name='user_commentlikes', blank=True)

class SitePost(models.Model):
    username = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
    )
    post = models.TextField(max_length=1024)
    postpic = models.ImageField(upload_to=site_post_upload_dir, null=True,blank=True)
    postdate = models.DateTimeField(auto_now_add=True)

class SiteSetting(models.Model):
    # This is a name value pair of various settings
    # for the site.
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

class FriendRequest(models.Model):
    # This table will hold the friend requests
    # and will be checked for someone to
    # answer request.
    request_by = models.ForeignKey(UserProfile, related_name='request_by', on_delete=models.CASCADE)
    request_to = models.ForeignKey(UserProfile, related_name='request_to', on_delete=models.CASCADE)
    request_answer = models.BooleanField(blank=True, null=True)
    request_date = models.DateTimeField(auto_now_add=True)
    answer_date = models.DateTimeField(blank=True, null=True)

class CollaborationGroup(models.Model):
    collaboration_group_name = models.CharField(max_length=255)
    collaboration_group_members = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.collaboration_group_name

class CollaborationGroupPost(models.Model):
    collaboration_group = models.ForeignKey(CollaborationGroup, on_delete=models.CASCADE)
    username = models.ForeignKey(UserProfile, related_name='group_post_username', on_delete=models.CASCADE)
    post = models.TextField(max_length=1024)
    postpic = models.ImageField(upload_to=group_post_upload_dir, blank=True,null=True)
    postdate = models.DateTimeField(auto_now_add=True)
    postlike = models.ManyToManyField(User, related_name='group_postlikes', blank=True)

class CollaborationGroupPostComment(models.Model):
    collaboration_group_post = models.ForeignKey(CollaborationGroupPost, on_delete=models.CASCADE)
    username = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1024)
    commentpic = models.ImageField(upload_to=group_comment_upload_dir, blank=True, null=True)
    commentdate = models.DateTimeField(auto_now_add=True)
    commentlike = models.ManyToManyField(User, related_name='group_commentlikes', blank=True)

class NavBarDropdown(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class NavBarDropdownCategory(models.Model):
    dropdown = models.ForeignKey(NavBarDropdown, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class NavBarLink(models.Model):
    dropdown = models.ForeignKey(NavBarDropdown, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(NavBarDropdownCategory, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=32)
    address = models.URLField()
    title = models.CharField(max_length=32)
    on_main_bar = models.BooleanField(default=False)
    icon = models.ImageField(upload_to=navbar_icon_upload_dir, null=True,blank=True)

    def __str__(self):
        return self.name

class Ad(models.Model):
    link = models.ForeignKey(NavBarLink, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description