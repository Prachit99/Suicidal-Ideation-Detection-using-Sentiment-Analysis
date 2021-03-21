from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os
import pandas as pd
import numpy as np
from . import utils

@login_required
def home(request):
    twitter_data = utils.twitter_scrape()
<<<<<<< HEAD
    reddit_data = []
=======
    #reddit_data = utils.reddit_scrape()
>>>>>>> 0db8e55b764b32b662e50c908f474f72852a10c5
    return render(request, "home.html", {'twitter': twitter_data, 'reddit': reddit_data})

def dataTable(request):
    return render(request, "dataTable.html")

def test(request):
    output = ""
    print(request.POST.get('platform','reddit'))
    raw_input = request.POST.get('text_post', 'is it strange when a part of you wishes to get corona with the hope to die?')
    if request.POST.get('platform', 'reddit') == 'twitter':
        output = utils.twitter_model(raw_input)
    else:
        output = utils.reddit_model(raw_input)
    return render(request, "test.html", {'input': raw_input, 'output': output})

