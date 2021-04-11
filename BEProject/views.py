from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from stats.models import Record
import os
import pandas as pd
import numpy as np
from . import utils

def test(request):
    output = ""
    platform = request.POST.get('platform', 'reddit')
    raw_input = request.POST.get('text_post', 'This is the suicidal ideation detection website!')
    if platform == 'twitter':
        output = utils.twitter_model(raw_input[:280])
        if output>0.9:
            final_output = 2
        elif output>0.7:
            final_output = 1
        else:
            final_output = 0
    else:
        output = utils.reddit_model(raw_input)
        if output>=0.95:
            final_output = 2
        elif output>=0.85:
            final_output = 1
        else:
            final_output = 0
    return render(request, "test.html", {'raw_input': raw_input,'final_output': final_output, 'output': output})

def annotate(request):
    if "GET" == request.method:
        return redirect("/accounts/login")
    csv_file = request.FILES["csv_file"]
    if not csv_file.name.endswith('.csv'):
        return redirect("/accounts/login")
    df = pd.read_csv(csv_file, encoding="ISO-8859-1")
    col1 = df.columns[0]
    posts = df[col1]
    df[col1] = df[col1].apply(str)
    df["output"] = df[col1].apply(utils.twitter_model)
    df["output"] = df["output"].apply(float)
    df.loc[df["output"]>=0.7, "class"] = "suicidal" 
    df.loc[df["output"]<0.7, "class"] = "not suicidal" 
    df[col1] = posts
    output_file = df.to_csv(index=False)
    response = HttpResponse(output_file, content_type='application/x-download')
    response['Content-Disposition'] = 'attachment;filename=table.csv'
    return response

@login_required
def record(request):
    records = Record.objects.all()
    return render(request, "records.html", {'records': records})
