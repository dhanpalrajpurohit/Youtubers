from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.
class Youtuber(models.Model):
    crew_choic = {
        ('solo','Solo'),
        ('dute','Dute'),
        ('small','Small'),
        ('large','Large'),
    }

    camera_choic = {
        ('sony','Sony'),
        ('nikon','Nikon'),
        ('canan','Canan'),
    }
    category_choic = {
        ('gaming','Gaming'),
        ('coding','Coding'),
        ('health','Health'),
    }
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/ytuber/%Y/%m')
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.IntegerField()
    video_url = models.CharField(max_length=255,default='')
    crew = models.CharField(choices=crew_choic,max_length=255)
    camera_type = models.CharField(choices=camera_choic,max_length=255)
    subs_count = models.IntegerField()
    category = models.CharField(choices=category_choic,max_length=255)
    is_feature = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now,blank=True)