from django.db import models
from datetime import datetime

# Create your models here.
class Videos(models.Model):
    title = models.CharField(max_length=4000, blank = True, null = True)
    description = models.CharField(max_length=4000, blank = True, null = True)
    datetime1 = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

