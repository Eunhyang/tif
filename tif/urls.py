from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^/(?P<time_id>\d+)$', views.record, name='record'),
]
