from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^welcome$', views.welcome),
    url(r'^add$', views.add),
    url(r'^adding$', views.adding),
    url(r'^edit$', views.edit),
    url(r'^update/(?P<number>\d+)$', views.update),
    url(r'^delete/(?P<number>\d+)$', views.delete),
    url(r'^profile/(?P<number>\d+)$', views.profile),
]
