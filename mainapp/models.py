from django.db import models

class Info(models.Model):
    person = models.CharField(max_length=100)
    stuff =  models.CharField(max_length=100)
    card =  models.CharField(max_length=100)
    content =  models.CharField(max_length=1000)
