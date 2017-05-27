from django.db import models
from django.utils import timezone
# Create your models here.

class Report(models.Model):
    name = models.CharField(max_length = 8, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return '{}'.format(self.id)

class Time(models.Model):
    report = models.ForeignKey(
        Report,
        related_name = "report_time",
        on_delete = models.CASCADE,
    )
    name = models.CharField(max_length = 5)
    activity = models.ManyToManyField('Activity', null=True, blank=True)
    feeling = models.ManyToManyField('Feeling', null=True, blank=True)
    memo = models.ManyToManyField('Memo', null=True, blank=True)
    def __str__(self):
        return self.name

class Activity(models.Model):
    content = models.CharField(max_length = 50)
    def __str__(self):
        return self.content

class Feeling(models.Model):
    feeling = models.CharField(max_length = 10)
    def __str__(self):
        return self.feeling

class Memo(models.Model):
    content = models.CharField(max_length = 200)
    def __str__(self):
        return self.content
