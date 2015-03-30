from django.conf.urls import patterns, include, url
from django.contrib import admin
import core.views as coreviews
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',

    url(r'^$', coreviews.LandingView.as_view()),
    url(r'location/$', coreviews.LocationListView.as_view()),
    url(r'search/$', coreviews.SearchListView.as_view()),
    url(r'location/(?P<pk>\d+)/detail/$', coreviews.LocationDetailView.as_view(), name='location_detail'),
    url(r'location/create/$', login_required(coreviews.LocationCreateView.as_view())),
    url(r'location/(?P<pk>\d+)/update/$', login_required(coreviews.LocationUpdateView.as_view()), name='location_update'),
    url(r'location/(?P<pk>\d+)/review/create/$', login_required(coreviews.ReviewCreateView.as_view()), name='review_create'),
    url(r'location/(?P<pk>\d+)/review/update/$', login_required(coreviews.ReviewUpdateView.as_view()), name='review_update'),
    url(r'entrance/$', coreviews.entrance),
)
