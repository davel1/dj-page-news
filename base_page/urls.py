from django.conf.urls import url

from base_page import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/', views.groups_list, name='gl'),
    url(r'^(?P<id>[0-9]+)/$', views.groups_details, name='gl_detail'),
    url(r'^(?P<id>[0-9]+)/(?P<hon>[0-9]+)/$', views.honor_details, name='honor_detail'),
    url(r'^profile/', views.profile),
    url(r'^set_stud/', views.set_stud, name='set_stud'),
]