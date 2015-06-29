from django.conf.urls import url

from faq import views

urlpatterns = [
    url(r'^$', views.index, name='faq'),
    url(r'^rest/', views.REST_faq_list, name='rest_list')
]

