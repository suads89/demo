from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import datetime

class Post(models.Model):
    title = models.CharField(max_length=400)
    content = models.CharField(max_length=4000)
    pub_date = models.DateTimeField('date published', null=True, blank=True)
    is_published = models.BooleanField(null= True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
