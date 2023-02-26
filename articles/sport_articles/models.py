from django.db import models
from django.urls import reverse



class Articles(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    url = models.URLField(max_length=200)
    published_time = models.CharField(max_length=100)
    img = models.URLField(max_length=300)



    def __str__(self):
        return self.title





class Meta:
    order = ["title"]

class Admin:
    pass


