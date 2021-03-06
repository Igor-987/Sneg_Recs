from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recs/$', views.RecList.as_view(), name='recs'),
    url(r'^rec/(?P<pk>\d+)$', views.RecDetailView.as_view(), name='rec_detail'),
    url(r'^rec/create/$', views.RecCreate.as_view(), name='rec_create'),
    url(r'^rec/(?P<pk>\d+)/update0/$', views.RecUpdate0.as_view(), name='rec_update0'),
    url(r'^rec/(?P<pk>\d+)/update1/$', views.RecUpdate1.as_view(), name='rec_update1'),
    url(r'^rec/(?P<pk>\d+)/update2/$', views.RecUpdate2.as_view(), name='rec_update2'),
    url(r'^rec/(?P<pk>\d+)/update3/$', views.RecUpdate3.as_view(), name='rec_update3'),
    url(r'^rec/(?P<pk>\d+)/update4/$', views.RecUpdate4.as_view(), name='rec_update4'),
    ]
