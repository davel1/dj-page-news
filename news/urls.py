from django.conf.urls import url

from news import views

urlpatterns = [
    url(r'^$', views.index, name='news'),
    url(r'^(?P<id>[0-9]+)/$', views.news_details, name='news_detail'),
]