#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import *

urlpatterns = patterns(('simpleTodo.views'),
    url(r'^$', 'todolist', name='todo'),
    url(r'^addtodo/$', 'addtodo', name='add'),
    url(r'^updatetodo/$', 'todoupdate', name='edit'),
    url(r'^tododelete/$', 'todoshanchu', name='shanchu'),
	url(r'^todofinish/$', 'wancheng', name='wancheng'),
    url(r'^todofinish/(?P<id>\d+)/$', 'todofinish', name='finish'),
    url(r'^todobackout/(?P<id>\d+)/$', 'todoback',  name='backout'),
    url(r'^updatetodo/(?P<id>\d+)/$', 'updatetodo', name='update'),
    url(r'^tododelete/(?P<id>\d+)/$', 'deletetodo', name='delete'),
)