from django.db import models
from django.utils import timezone
# Create your models here.

class Report(models.Model):
    time = models.ManyToManyField('Time')
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
            return self.created_date

class Time(models.Model):
    name = models.CharField(max_length = 5)
    activity = models.ManyToManyField('Activity')
    feeling = models.ManyToManyField('Feeling')
    memo = models.ManyToManyField('Memo')
    def __str__(self):
            return self.created_date

class Activity(models.Model):
    content = models.CharField(max_length = 50)
    def __str__(self):
        return self.content

class Feeling(models.Model):
    AGNER = 'ag'
    SADNESS = 'sd'
    JOY = 'jy'
    DISCUST = 'dc'
    FEAR = 'fr'
    CATEGORY_CHOICES = (
        (AGNER, 'anger'),
        (SADNESS, 'sadness'),
        (JOY, 'joy'),
        (DISCUST, 'discust'),
        (FEAR, 'fear'),
    )
    category = models.CharField(
        max_length = 2,
        choices = CATEGORY_CHOICES,
        default = JOY,
    )
    def __str__(self):
        return self.category

class Memo(models.Model):
    content = models.CharField(max_length = 200)
    def __str__(self):
        return self.content
