#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from ..views.sprite_feed import LatestEntriesFeed

urlpatterns = patterns("spirit.views.sprite_feed",
    url(r'^$', LatestEntriesFeed(), name='latest_entries_feed'),
)