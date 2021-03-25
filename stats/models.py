from django.db import models

# Create your models here.

platform_choices = [("twitter","twitter"),("reddit", "reddit")]

class Record(models.Model):
    userid = models.CharField(max_length=20)
    username = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField(auto_now=True)
    platform = models.CharField(choices=platform_choices, max_length=7)
    output = models.FloatField(default=-1.0)
    
    def __str__(self):
        return self.content

