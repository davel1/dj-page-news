from django.conf.urls import url

from base_page import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]