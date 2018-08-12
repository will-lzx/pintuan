from django.db import models

# Create your models here.


class Customer(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    openid = models.CharField(max_length=200)
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField(auto_now=True)


class Issue(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    issue_type = models.IntegerField()
    description = models.TextField()
    owner = models.CharField(max_length=200)
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField(auto_now=True)
