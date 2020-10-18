# simplesocial2/urls.py
from django.urls import path
#from .views import HomePageView
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('simplesocial2/sitepost/add', views.AddSitePostView.as_view(), name="add_site_post"),
]
