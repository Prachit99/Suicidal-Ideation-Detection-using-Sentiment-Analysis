from django.shortcuts import render
from django.http import HttpResponse
from stats.models import Record
from BEProject.utils import twitter_scrape, reddit_scrape
import pandas as pd
from .models import Record
# Create your views here.

def index(request):
    df1 = twitter_scrape()
    df2 = reddit_scrape()
    row_iter = df1.iterrows()
    objs = [
        Record(
            userid = row['userid'],
            username = row['username'],
            content = row['post'],
            created = row['created'],
            platform = row['platform']
        )
        for index, row in row_iter
    ]
    Record.objects.bulk_create(objs)
    row_iter = df2.iterrows()
    objs = [
        Record(
            userid = row['userid'],
            username = row['username'],
            content = row['post'],
            created = row['created'],
            platform = row['platform']
        )
        for index, row in row_iter
    ]
    Record.objects.bulk_create(objs)
    return HttpResponse('Loading data into database')
