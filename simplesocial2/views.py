from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView
from . import models
from . import forms
from django import forms as djforms
from django.forms import modelform_factory
from django.db.models import Q
# Create your views here.

def homepage(request):
    try:
        site_name = models.SiteSetting.objects.get(name='sitename')
    except models.SiteSetting.DoesNotExist:
        site_name = {'value':'Simple Social Media'}

    sitepost = models.SitePost.objects.order_by('-postdate')
    context = {'site_name':site_name, 'sitepost':sitepost, 'current_user':request.user}
    
    # If the this view is loaded with a logged in user
    # thne pull the the posts for that specific user
    if request.user.is_authenticated:
        userpost = models.UserPost.objects.filter(username__username=request.user).order_by('-postdate')
        context['userpost'] = userpost

        myfriends = models.UserProfile.objects.get(username__username=request.user).friends.all()
        context['myfriends'] = myfriends

        friendpost = []
        for x in myfriends:
            friendpost += models.UserPost.objects.filter(username__username__username=x.username)
        '''
        friendpost = models.UserPost.objects.filter(username__username__username='dpost')
        '''
        context['friendpost'] = friendpost
        
    
    return render(request, 'simplesocial2/home.html', context)

class HomePageView(TemplateView):
    template_name = 'simplesocial2/home.html'

class AddSitePostView(LoginRequiredMixin, CreateView):
    #model = models.SitePost
    #username = djforms.HiddenInput()
    #form_class = forms.AddSitePostForm
    form_class = modelform_factory(models.SitePost, form=forms.AddSitePostForm, fields='__all__', widgets={'username': djforms.HiddenInput()})
    template_name = 'simplesocial2/sitepost.html'
    #fields = ['post','postpic','username']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)