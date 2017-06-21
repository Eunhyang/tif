from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'tif'
urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^add/$', views.report_add, name='report_add'),
    url(r'^(?P<report_id>\d+)/delete/$', views.report_delete, name="report_delete"),
    url(r'^record/$', views.record, name='record'),
    url(r'^time/data/$', views.time_data, name='time_data'),
    url(r'^memo/add/$', views.memo_add, name='memo_add'),
    url(r'^memo/data/$', views.memo_data, name='memo_data'),
    url(r'^memo/edit/$', views.memo_edit, name='memo_edit'),

    url(r'^logout/$', auth_views.logout, name='logout', kwargs={'next_page': 'tif:index'}),
]
