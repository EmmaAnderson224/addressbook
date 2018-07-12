# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.views import generic

from .models import Address

class IndexView(generic.ListView):
    model = Address
    template_name = 'address_list.html'