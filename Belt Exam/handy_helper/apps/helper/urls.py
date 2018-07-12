from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^welcome$', views.welcome),
    url(r'^add$', views.add),
    url(r'^adding$', views.adding),
    url(r'^job/(?P<number>\d+)$', views.job),
    url(r'^join/(?P<number>\d+)$', views.join),
    url(r'^cancel/(?P<number>\d+)$', views.cancel),
    url(r'^delete/(?P<number>\d+)$', views.delete),
    url(r'^edit/(?P<number>\d+)$', views.edit),
    url(r'^update/(?P<number>\d+)$', views.update),
]