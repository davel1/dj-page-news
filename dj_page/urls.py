"""dj_page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from base_page import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^faq/', include('faq.urls')),
    url(r'', include('base_page.urls')),
    url(r'^gl/', include('base_page.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^accounts/login/$', views.signin, name='auth'),
    url(r'^accounts/logout/$', views.logout_views, name='auth_logout'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^set_stud/', views.set_stud, name='set_stud'),
    url('', include('social.apps.django_app.urls', namespace='social')),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)