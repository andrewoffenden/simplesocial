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
    list_display = ['username', 'post']

admin.site.register(ssoc.SitePost, SitePostAdmin)

class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']

admin.site.register(ssoc.SiteSetting, SiteSettingAdmin)

class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ['request_by', 'request_to', 'request_answer', 'request_date', 'answer_date']

admin.site.register(ssoc.FriendRquest, FriendRequestAdmin)

class CollaborationGroupAdmin(admin.ModelAdmin):
    pass

admin.site.register(ssoc.CollaborationGroup, CollaborationGroupAdmin)

class CollaborationGroupPostAdmin(admin.ModelAdmin):
    pass

admin.site.register(ssoc.CollaborationGroupPost, CollaborationGroupPostAdmin)

class CollaborationGroupPostCommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(ssoc.CollaborationGroupPostComment, CollaborationGroupPostCommentAdmin)

class NavBarDropdownAdmin(admin.ModelAdmin):
    pass

admin.site.register(ssoc.NavBarDropdown, NavBarDropdownAdmin)

class NavBarDropdownCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(ssoc.NavBarDropdownCategory, NavBarDropdownCategoryAdmin)

class NavBarLinkAdmin(admin.ModelAdmin):
    pass

admin.site.register(ssoc.NavBarLink, NavBarLinkAdmin)

class AdAdmin(admin.ModelAdmin):
    pass

admin.site.register(ssoc.Ad, AdAdmin)