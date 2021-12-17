from django.forms import ModelForm
from . import models
from django import forms

class AddSitePostForm(forms.Form, ModelForm):
    class Meta:
        postby = forms.HiddenInput(attrs={'name':'username'})
        model = models.SitePost
        fields = ['post','postpic']

class AddUserPostForm(ModelForm):
    
    class Meta:
        model = models.UserPost
        fields = '__all__'