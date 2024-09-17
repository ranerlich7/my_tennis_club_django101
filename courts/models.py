from django.db import models

class Courts(models.Model):
    number = models.IntegerField(default=0, null=False,unique=True)
    is_occupied = models.BooleanField(default=False)
    time_occupied = models.DateTimeField(null=True)
    
