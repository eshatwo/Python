from django.conf.urls import url
from . import views   
urlpatterns = [
    url(r'^$', views.survey),
    url(r'^result/$', views.result),
]