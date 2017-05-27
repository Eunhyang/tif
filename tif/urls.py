from django.conf.urls import url
from . import views

app_name = 'tif'
urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^record/$', views.record, name='record'),
]
