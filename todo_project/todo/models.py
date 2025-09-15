from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100)
    task = models.TextField()
    date_of_reminder = models.DateField()
    time_description = models.TimeField()

    def __str__(self):
        return self.task