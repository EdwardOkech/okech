from django.db import models
from django.contrib.auth.models import User
import random


class Portfolio(models.Model):
    TYPE = (
        ('os','Open Source'),
        ('pr','Propretory'),
        )
    title = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100, choices=TYPE,verbose_name='project type')
    client = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.title

    

class Contact(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    address = models.CharField(max_length=100)
    sender = models.EmailField(max_length=75)
    
    def __unicode__(self):
        return self.subject


''' I am the guy your parents warned you about....am a 3rd generation anarchist who consumes
gargantuan quantities of pot,hash,acid and peyote.hasn't had an unhalucinated day since 1985
.easy to arouse, hard to pacify and most people just go away,some say am a verb but i think am a gerund..'''
