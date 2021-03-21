from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os
import tweepy as tw
import pandas as pd
from datetime import date
import numpy as np
from tensorflow.keras.models import model_from_json
import tensorflow_hub as hub


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
    date_since = 19-3-21
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
    output = ""
    with open('Models/model.json', 'r') as f: 
        json = f.read() 
    loaded_model = model_from_json(json, custom_objects={'KerasLayer': hub.KerasLayer})

    # load weights into new model
    loaded_model.load_weights("Models/model.h5")
    print("Loaded model from disk")
    raw_input = request.POST.get('text_post', 'is it strange when a part of you wishes to get corona with the hope to die?')
    # evaluate loaded model on test data
    output = loaded_model.predict(np.array([raw_input]))
    return render(request, "test.html", {'output': output})

