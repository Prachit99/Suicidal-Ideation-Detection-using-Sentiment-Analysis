from django.http import HttpResponse
from django.shortcuts import render, redirect
import joblib

def login(request):
    return render(request, "login.html")

def home(request):
    return render(request, "home.html")

def test(request):
    #cls = joblib.load("model.sav")
    output = request.POST.get('text_post', False)
    #    output = cls.predict([raw_text])
    return render(request, "test.html", {'output': output})

