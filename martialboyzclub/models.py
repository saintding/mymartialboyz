from django.db import models

from django.contrib.contenttypes.fields import GenericRelation, GenericRel,GenericForeignKey

from django.contrib.contenttypes.models import  ContentType

# Create your models here.
class collectionclass(models.Model):

    name = models.CharField(max_length=128,verbose_name='课程名称')

    course_img = models.CharField(max_length=255,verbose_name='课程缩略图')

    brief = models.TextField(max_length=320,verbose_name='课程简介')

    total_scholarship = models.PositiveIntegerField(verbose_name='总奖学金',default=6000)

    assistant_coach = models.PositiveIntegerField(verbose_name='陪练费用',default=8000)

    period = models.PositiveIntegerField(verbose_name='建议学习天数',default=365,help_text='方便计算返利时使用')
    prerequisite = models.TextField(verbose_name='课程前提',max_length=1024)

    coach = models.ManyToManyField(verbose_name='教练',to="coachinfo")

    class Meta:

        db_table = 'collectionclass'


class coachinfo(models.Model):

    name = models.CharField(verbose_name='教练姓名',max_length=32)

    image = models.CharField(verbose_name='头像',max_length=255)

    footstep = models.CharField(verbose_name='足迹',max_length=255,blank=True,null=True)

    source = ((1,'体育学院'),(2,'武术学校'),(3,'军警/作战部队'),(4,'保镖训练营'),(5,'武馆'))

    background = models.SmallIntegerField(choices=source,default=1)

    roles = ((1,'教练'),(2,'陪练'))

    role = models.SmallIntegerField(choices=roles,default=1)

    brief = models.TextField(max_length=1024,verbose_name='简介')

    class Meta:

        db_table = 'coachinfo'

class pricecondition(models.Model):

    '''课程定价策略这里用content-type建立表与表之间对象的联系'''

    # '''课程定价策略这里用content-type建立表与表之间对象的联系'''
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE,verbose_name='建立与集体课或私教之间的联系')

    object_id = models.PositiveIntegerField(verbose_name='建立与关联表对象之间的主键关联')

    content_obj = GenericForeignKey('content_type','object_id')

    period_choices = (
        (1, '1次'),
        (3, '3次'),
        (7, '7次'),
        (14, '2周'),
        (30, '1个月'),
        (60, '2个月'),
        (90, '3个月'),
        (180, '6个月'),
        (210, '12个月'),
        (540, '18个月'),
        (720, '24个月'),
    )

    valid_period = models.SmallIntegerField(choices=period_choices,verbose_name='时长')

    price = models.FloatField(verbose_name='价格')