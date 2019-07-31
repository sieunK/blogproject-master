from django.db import models
from django.utils import timezone
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date_published')
    description = models.TextField(blank=True, null=False)
    make_date = models.DateTimeField(default = timezone.now)


    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:50]
