from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recs/$', views.rec_list, name='recs'),
    url(r'^rec/(?P<pk>\d+)$', views.RecDetailView.as_view(), name='rec-detail'),
    url(r'^rec/create/$', views.RecCreate.as_view(), name='rec_create'),
]