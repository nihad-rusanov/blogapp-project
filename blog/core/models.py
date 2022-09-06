from django.db import models

class Blog_Model(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()


# Create your models here.
