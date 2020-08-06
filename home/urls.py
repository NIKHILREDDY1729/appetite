from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.Feed, name='Feed'),
    path("Browse", views.Browse, name='Browse'),
    path("Login", views.Login, name='Login'),
    path("Articles", views.Articles, name='Articles'), 
    path("Register", views.Register, name='Register'),
    path("userprofile", views.userprofile, name='userprofile'), 
    path("form", views.form, name='form'), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)