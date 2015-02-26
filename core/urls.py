from django.conf.urls import patterns, include, url
from django.contrib import admin
import core.views as coreviews

urlpatterns = patterns('',

    url(r'^$', coreviews.LandingView.as_view()),
)
