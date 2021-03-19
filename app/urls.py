from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recs/$', views.RecListView.as_view(), name='recs'),
    url(r'^rec/(?P<pk>\d+)$', views.RecDetailView.as_view(), name='rec-detail'),
]