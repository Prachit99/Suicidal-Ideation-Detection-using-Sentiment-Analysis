from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os
import pandas as pd
import numpy as np
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow_hub as hub
import pickle
from . import utils

@login_required
def home(request):
    df = utils.twitter_scrape()
    return render(request, "home.html", {'df': df})

def test(request):
    output = ""
    print(request.POST.get('platform','reddit'))
    if request.POST.get('platform', 'reddit') == 'twitter':
        raw_input = request.POST.get('text_post', 'is it strange when a part of you wishes to get corona with the hope to die?')
        raw_input = utils.preprocess_tweet(raw_input)
        with open('Models/tokenizer.pickle', 'rb') as handle:
            tokenizer = pickle.load(handle)

        seq = tokenizer.texts_to_sequences([raw_input])
        padded_sequence = pad_sequences(seq, maxlen=200)
        with open('Models/model_t.json', 'r') as f: 
            json = f.read() 
        loaded_model = model_from_json(json)

        # load weights into new model
        loaded_model.load_weights("Models/model_t.h5")
        output = loaded_model.predict(padded_sequence)

    else:
        with open('Models/model_r.json', 'r') as f: 
            json = f.read() 
        loaded_model = model_from_json(json, custom_objects={'KerasLayer': hub.KerasLayer})

        # load weights into new model
        loaded_model.load_weights("Models/model_r.h5")
        raw_input = request.POST.get('text_post', 'is it strange when a part of you wishes to get corona with the hope to die?')
        # evaluate loaded model on test data
        output = loaded_model.predict(np.array([raw_input]))
    return render(request, "test.html", {'input': raw_input, 'output': output})

