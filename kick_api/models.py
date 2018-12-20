from django.db import models

#c Create your models here.
class KickStarter(models.Model):
    backers_count = models.IntegerField()
    blurb = models.TextField()
    category = models.TextField()

    class Meta:
        ordering = ['backers_count']
