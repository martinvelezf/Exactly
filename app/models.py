# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Incident(models.Model):
    STATUS = (
       ('open', ('open')),
       ('close', ('close')),
    )
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=564)
    status=models.CharField(max_length=9, choices=STATUS,default='open')
    start_date=models.DateTimeField()
    end_date=models.DateTimeField(blank=True,null=True)
    def __str__(self):
       return '{} {}'.format(self.title, self.status)


class Updates(models.Model):
    TYPES = (
       ('Resolution', ('Resolution')),
       ('Update', ('Update')),
       ('Investigation', ('Investigation')),
    )
    incident = models.ForeignKey(Incident, related_name="update", on_delete=models.CASCADE)
    content=models.CharField(max_length=564)
    date=models.DateTimeField()
    type=models.CharField(max_length=25, choices=TYPES)
    def __str__(self):
       return '{} {}'.format(self.content, self.type)