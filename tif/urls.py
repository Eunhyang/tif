from django.conf.urls import url
from . import views

app_name = 'tif'
urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^add/$', views.report_add, name='report_add'),
    url(r'^record/$', views.record, name='record'),
    url(r'^memo/add/$', views.memo_add, name='memo_add'),
]
