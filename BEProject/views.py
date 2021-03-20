from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import joblib
import os
import tweepy as tw
import pandas as pd
from datetime import date


@login_required
def home(request):
    consumer_key = '1ljbylLYSgk6FIpepCzhQVKUE'
    consumer_secret = 'WGIsKEobyGx2FbS3uvZfVMeFAOwMmusvGCTqjuSnqbU7TQI4N3'
    access_token = '839721048538914817-01LEnkpGcjdDXL8grKxJ8r7UvrkVqQ6'
    access_token_secret = 'GgByKXcBqQoW0G3sz4clhNWryOWCKKHzFkVn0yscHSkej'
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    search_words = ["suicide","suicidal","mentalhealth","selfharm","hatemyself","iwanttodie"]
    date_since = date.today()
    tweetstore = []
    for search_word in search_words:
        # Collect tweets
        tweets = tw.Cursor(api.search,
                    q=search_word,
                    lang="en",
                    since=date_since).items(10)
        # Collect a list of tweets
        for tweet in tweets:
            tweetstore.append(tweet.text) 
    df = pd.DataFrame({'Posts': tweetstore})
    return render(request, "home.html", {'df': df})

def test(request):
    #cls = joblib.load("model.sav")
    output = request.POST.get('text_post', False)
    #    output = cls.predict([raw_text])
    return render(request, "test.html", {'output': output})

