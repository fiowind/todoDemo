#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models


class Todo(models.Model):
    user = models.CharField(max_length=50)
    todo = models.CharField(max_length=50)
    # 1 for undo, 0 for done
    flag = models.IntegerField(max_length=2, default=1)
    priority = models.CharField(max_length=2)
    pubtime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%d %s %s' % (self.id, self.todo, self.flag)

    class Meta:
        ordering = ['priority', 'pubtime']
