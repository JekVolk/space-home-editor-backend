from django.db import models
from django.utils import timezone


class OrientedMixin(models.Model):
    orient = models.IntegerField()

    class Meta:
        abstract=True


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ValueResourceMixin(models.Model):
    value=models.IntegerField()
    is_disposable= models.BooleanField(False)

    class Meta:
        abstract = True


class Size2DMixin(models.Model):
    w = models.PositiveIntegerField()
    h = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Size3DMixin(models.Model):
    w = models.PositiveIntegerField()
    h = models.PositiveIntegerField()
    d = models.PositiveIntegerField()

    class Meta:
        abstract = True


class BasePropertyMixin(models.Model):
    name=models.CharField(max_length=50)
    price=models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)
    comment=models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class CordMixin(models.Model):
    x = models.PositiveIntegerField()
    y = models.PositiveIntegerField()
    z = models.PositiveIntegerField()


    class Meta:
        abstract = True
