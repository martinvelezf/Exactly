# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import *
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def show_incident(request):
    context={'incident':Incident.objects.all()}
    return render(request, 'index.html', context)

@require_http_methods(["GET"])
def show_updates(request,id_inc):
    a=Incident.objects.get(id=id_inc)
    context={'incident':Incident.objects.get(id=id_inc)}
    return render(request, 'update.html', context)