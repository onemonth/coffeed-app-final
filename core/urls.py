from django.conf.urls import patterns, include, url
from django.contrib import admin
import core.views as coreviews

urlpatterns = patterns('',

    url(r'^$', coreviews.LandingView.as_view()),
    url(r'location/$', coreviews.LocationListView.as_view()),
    url(r'location/(?P<pk>\d+)/detail/$', coreviews.LocationDetailView.as_view(), name='location_list'),
)
