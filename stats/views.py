from django.shortcuts import render
from django.http import HttpResponse
from stats.models import Record
from BEProject.utils import twitter_scrape, reddit_scrape, reddit_model, twitter_model
import pandas as pd
from .models import Record
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

# Create your views here.

@login_required
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
    try:
        Record.objects.bulk_create(objs)
    except IntegrityError as e:
        print("data duplicate")
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
    try:
        Record.objects.bulk_create(objs)
    except IntegrityError as e:
        print("data duplicate")
    count = 0
    filter_columns = Record.objects.values_list('id', 'content', 'platform')
    for row in filter_columns:
        if row[2] == "twitter":
            output, sarcasm_op = twitter_model(row[1])
            if output>0.9:
                output = 2
            elif output>0.7:
                output = 1
            else:
                output = 0

            if sarcasm_op > 0.7:
                sarcasm = True
            else:
                sarcasm = False
            
        else:
            output = reddit_model(row[1])
            if output<=0.09:
                output = 2
            elif output<=0.15:
                output = 1
            else:
                output = 0
        Record.objects.filter(id=row[0]).update(output=output)
        count = count+1
        print(count)

    return HttpResponse('Loading data into database')
