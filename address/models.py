# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Address(models.Model):
    firstname = models.CharField('firstname', max_length=40, default='')
    lastname = models.CharField('lastname', max_length=40, default='')
    gender = models.CharField('sex', choices=(('M', 'male'), ('F', 'female')),
        max_length=1)
    email = models.CharField('email', max_length=40, default='')
    telphone = models.CharField('telephone', max_length=20, unique=True)
    notes = models.CharField('notes', max_length=50, default='')

    def __str__(self):
        return self.firstname + '_' + self.lastname
    
