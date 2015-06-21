from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new/$', views.new_entry, name='new_entry'),
    url(r'^(?P<billing_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.index, name='index'),
]
