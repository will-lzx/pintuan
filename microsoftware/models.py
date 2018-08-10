from django.db import models


# Create your models here.


class Customer(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    openid = models.CharField(max_length=200)
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField(auto_now=True)


class Production(models.Model):
    """
    产品表
    """
    id = models.IntegerField(primary_key=True, auto_created=True)
    category = models.IntegerField()
    brand = models.IntegerField()
    price = models.FloatField(default=0)
    pin_price = models.FloatField(default=0)
    status = models.IntegerField()
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField(auto_now=True)


class ShareRelation(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    owner = models.CharField(max_length=200)
    share = models.CharField(max_length=200)
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField(auto_now=True)


class ReceiveInfo(models.Model):
    """
    用户收货地址
    """
    id = models.IntegerField(primary_key=True, auto_created=True)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    author = models.CharField(max_length=200)
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField(auto_now=True)


class Order(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    owner = models.CharField(max_length=200)
    product = models.ForeignKey(Production, on_delete=True)
    price = models.FloatField()
    receive = models.ForeignKey(ReceiveInfo, on_delete=True)
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField(auto_now=True)

    ##############################################################
    # 净水器模块
    #
    ##############################################################


class Water(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    price = models.FloatField()
    # 提成暂时只有两种，10%，15%
    payment = models.FloatField()
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField(auto_now=True)


class User(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    is_agent = models.BooleanField(default=False)
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField(auto_now=True)


class AgentRelation(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    owner = models.CharField(max_length=200)
    share = models.CharField(max_length=200)
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField(auto_now=True)
