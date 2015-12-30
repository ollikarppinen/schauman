# -*- coding: utf-8 -*-
from django.shortcuts import render
import datetime
from django.utils.timezone import now


def home(request):
    context = {}
    context['today'] = datetime.date.today()
    context['now'] = now()
    return render(request, "schauman/index.html", context)


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")
