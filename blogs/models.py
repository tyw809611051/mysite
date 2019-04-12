from django.db import models

# Create your models here.
class Article(models.Model):
    title   = models.CharField(max_length=255)
    picture = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    excerpt = models.CharField(max_length=255)
    author  = models.CharField(max_length=125)
    users_id= models.IntegerField(default=0)
    tag     = models.CharField(max_length=100)
    status  = models.IntegerField(default=1)
    category_id = models.IntegerField(default=0)
    created_at  = models.DateTimeField('date created_at')
    updated_at  = models.DateTimeField('date updated_at')
