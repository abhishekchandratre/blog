from django.db import models

# Create your models here.
class Blog_details(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    path = models.CharField(max_length=4096)
    tags = models.CharField(max_length=200)
    pub_date = models.DateField('date published')

