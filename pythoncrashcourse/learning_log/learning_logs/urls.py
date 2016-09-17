"""Defines URL patterns for learning_logs."""

from django.conf.urls import url
from . import views

urlpatterns = [
    #homepage
    url(r'^$', views.index, name = 'index'),
    url(r'^topics/$', views.topics, name = 'topics'),
        #detail page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),
    url(r'^new_topic/$', views.new_topic, name = 'new_topic'),
    ]