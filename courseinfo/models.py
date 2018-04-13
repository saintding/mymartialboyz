from django.db import models

from django.contrib.contenttypes.models import ContentType

from django.contrib.contenttypes.fields import  GenericForeignKey,GenericRelation

# Create your models here.

class coursetype(models.Model):

    typename = models.CharField(verbose_name='形式类别',max_length=30)

    class Meta:

        db_table = 'coursetype'

class coursecontent(models.Model):

    contentname = models.CharField(verbose_name='课程分类',max_length=32)

    class Meta:


        db_table = 'coursecontent'
