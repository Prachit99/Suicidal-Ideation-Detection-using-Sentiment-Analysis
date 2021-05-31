from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Count
from plotly.offline import plot
from plotly.graph_objs import Bar, Scatter
import datetime

from stats.models import Record
import pandas as pd
from . import utils

def test(request):
    output = ""
    platform = request.POST.get('platform', 'reddit')
    sarc_content = -1
    raw_input = request.POST.get('text_post', 'This is the suicidal ideation detection website!')
    if platform == 'twitter':
        output, sarc_op = utils.twitter_sarcasm(raw_input[:280])
        if output>0.9:
            final_output = 2
        elif output>0.7:
            final_output = 1
        else:
            final_output = 0
        if sarc_op>0.7:
            sarc_content = 1
        else:
            sarc_content = 0
        return render(request, "test.html", {'raw_input': raw_input,'final_output': final_output, 'output': output, 'sarc_content': sarc_content})

    else:
        output = utils.reddit_model(raw_input)
        if output>=0.85:
            final_output = 2
        elif output>=0.65:
            final_output = 1
        else:
            final_output = 0
        return render(request, "test.html", {'raw_input': raw_input,'final_output': final_output, 'output': output, 'sarc_content': sarc_content})

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
    platform = request.POST.get('platform', 'reddit')
    if platform == "twitter":
        df["output"] = df[col1].apply(utils.twitter_model)
    else:
        df["output"] = df[col1].apply(utils.reddit_model)
    df["output"] = df["output"].apply(float)
    df.loc[df["output"]>=0.7, "class"] = "suicidal" 
    df.loc[df["output"]<0.7, "class"] = "not suicidal" 
    df[col1] = posts
    del df['output']
    output_file = df.to_csv(index=False)
    response = HttpResponse(output_file, content_type='application/x-download')
    response['Content-Disposition'] = 'attachment;filename=table.csv'
    return response

@login_required
def record(request):
    records = Record.objects.all()
    return render(request, "records.html", {'records': records})

@login_required
def charts(request):
    records = Record.objects.filter(platform="twitter").values('username','output').annotate(count = Count('output')).values_list('username', 'output', 'count').order_by('username')
    print(records)
    x1_data = []
    x2_data = []
    x3_data = []
    y1_data = []
    y2_data = []
    y3_data = []
    for row in records:
        if row[1] == 0:
            x1_data.append(row[0])
            y1_data.append(row[2])
        elif row[1] == 1:
            x2_data.append(row[0])
            y2_data.append(row[2])
        elif row[1] == 2:
            x3_data.append(row[0])
            y3_data.append(row[2])
    plot_low = plot([Bar(x=x1_data, y=y1_data)], output_type='div')
    plot_med = plot([Bar(x=x2_data, y=y2_data)], output_type='div')
    plot_high = plot([Bar(x=x2_data, y=y2_data)], output_type='div')
    return render(request, "charts.html", context={'plot_low': plot_low, 'plot_med': plot_med, 'plot_high': plot_high})
