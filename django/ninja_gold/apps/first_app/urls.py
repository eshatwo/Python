from django.conf.urls import url
from . import views   
urlpatterns = [
    url(r'^$', views.process),
    url(r'^process_money/$', views.money),
    url(r'^clear/$', views.clear),
]
