from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recs/$', views.rec_list, name='recs'),
    url(r'^rec/(?P<pk>\d+)$', views.RecDetailView.as_view(), name='rec_detail'),
    url(r'^rec/create/$', views.RecCreate.as_view(), name='rec_create'),
    url(r'^rec/(?P<pk>\d+)/update/$', views.RecUpdate1.as_view(), name='rec_update1'),
]