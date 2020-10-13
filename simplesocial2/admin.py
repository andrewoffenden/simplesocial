from django.contrib import admin
#from django.contrib.auth import get_user_model
#from django.contrib.auth.admin import UserAdmin
#from .models import UserProfile, UserPost, UserPostComment, SitePost
from . import models as ssoc

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username']

admin.site.register(ssoc.UserProfile, UserProfileAdmin)

class UserPostAdmin(admin.ModelAdmin):
    pass

admin.site.register(ssoc.UserPost, UserPostAdmin)

class UserPostCommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(ssoc.UserPostComment, UserPostCommentAdmin)

class SitePostAdmin(admin.ModelAdmin):
    pass

admin.site.register(ssoc.SitePost, SitePostAdmin)

class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']

admin.site.register(ssoc.SiteSetting, SiteSettingAdmin)