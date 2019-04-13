from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

"""
标题模型
"""
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

    def __str__(self):
        return self.title

    def was_created_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)


"""
分类模型
"""
class Category(models.Model):
    name = models.CharField(max_length=255)
    feature_id = models.IntegerField(max_length=11,blank=True)
    parent_id  = models.IntegerField(max_length=11,blank=True)
    status = models.IntegerField(max_length=6,blank=True)
    created_at = models.DateTimeField("date created_at",blank=True)
    updated_at = models.DateTimeField("date updated_at",blank=True)

    def __str__(self):
        return self.name

"""
评论模型
"""
class Comment(models.Model):
    content = models.CharField(max_length=255)
    parent_id = models.IntegerField(max_length=11,blank=True)
    article_id = models.IntegerField(max_length=11,blank=True)
    member_id = models.IntegerField(max_length=11,blank=True)
    status = models.IntegerField(max_length=6,blank=True)
    created_at = models.DateTimeField("date created_at",blank=True)
    updated_at = models.DateTimeField("date updated_at",blank=True)

    def __str__(self):
        return self.content

"""
板块模型
"""
class Feature(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255,blank=True)
    status = models.IntegerField(max_length=6,blank=True)
    sort = models.IntegerField(max_length=6,blank=True)
    created_at = models.DateTimeField("date created_at",blank=True)
    updated_at = models.DateTimeField("date updated_at",blank=True)

    def __str__(self):
        return self.name

"""
信息模型
"""
class Message(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255,blank=True)
    status = models.IntegerField(max_length=6,blank=True)
    created_at = models.DateTimeField("date created_at",blank=True)
    updated_at = models.DateTimeField("date updated_at",blank=True)