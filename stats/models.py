from django.db import models
# Create your models here.

platform_choices = [("twitter","twitter"),("reddit", "reddit")]
output_choices = [("0", "Low"), ("1", "Medium"), ("2", "High"), ("-1", "Untested")]

class Record(models.Model):
    userid = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    content = models.TextField(unique=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(auto_now=True)
    platform = models.CharField(choices=platform_choices, max_length=7)
    output = models.IntegerField(default=-1, choices = output_choices)
    
    def __str__(self):
        return self.content

class User(models.Model):
    userid = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    low_si = models.TextField()
    med_si = models.TextField()
    high_si = models.TextField()
    platform = models.CharField(choices=platform_choices, max_length=7)
    
    def __str__(self):
        return self.content

