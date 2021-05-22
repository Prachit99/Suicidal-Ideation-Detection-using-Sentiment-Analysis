from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import model_from_json
from tensorflow.keras.models import load_model
import tensorflow as tf
import tensorflow_hub as hub
import pickle
import preprocessor as p
import re
import tweepy as tw
from datetime import date
import pandas as pd
import numpy as np
import time
from datetime import datetime
import praw
import nltk
stopwords = nltk.download('stopwords')
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer
import string

def preprocess_tweet(tweet):
    # Contractions
    tweet = re.sub(r"\x89Ûª", "'", tweet)
    tweet = re.sub(r"he's", "he is", tweet)
    tweet = re.sub(r"there's", "there is", tweet)
    tweet = re.sub(r"We're", "We are", tweet)
    tweet = re.sub(r"That's", "That is", tweet)
    tweet = re.sub(r"won't", "will not", tweet)
    tweet = re.sub(r"they're", "they are", tweet)
    tweet = re.sub(r"Can't", "Cannot", tweet)
    tweet = re.sub(r"wasn't", "was not", tweet)
    tweet = re.sub(r"don\x89Ûªt", "do not", tweet)
    tweet = re.sub(r"aren't", "are not", tweet)
    tweet = re.sub(r"isn't", "is not", tweet)
    tweet = re.sub(r"What's", "What is", tweet)
    tweet = re.sub(r"haven't", "have not", tweet)
    tweet = re.sub(r"hasn't", "has not", tweet)
    tweet = re.sub(r"There's", "There is", tweet)
    tweet = re.sub(r"He's", "He is", tweet)
    tweet = re.sub(r"It's", "It is", tweet)
    tweet = re.sub(r"You're", "You are", tweet)
    tweet = re.sub(r"I'M", "I am", tweet)
    tweet = re.sub(r"shouldn't", "should not", tweet)
    tweet = re.sub(r"wouldn't", "would not", tweet)
    tweet = re.sub(r"i'm", "I am", tweet)
    tweet = re.sub(r"I\x89Ûªm", "I am", tweet)
    tweet = re.sub(r"I'm", "I am", tweet)
    tweet = re.sub(r"Isn't", "is not", tweet)
    tweet = re.sub(r"Here's", "Here is", tweet)
    tweet = re.sub(r"you've", "you have", tweet)
    tweet = re.sub(r"you\x89Ûªve", "you have", tweet)
    tweet = re.sub(r"we're", "we are", tweet)
    tweet = re.sub(r"what's", "what is", tweet)
    tweet = re.sub(r"couldn't", "could not", tweet)
    tweet = re.sub(r"we've", "we have", tweet)
    tweet = re.sub(r"it\x89Ûªs", "it is", tweet)
    tweet = re.sub(r"doesn\x89Ûªt", "does not", tweet)
    tweet = re.sub(r"It\x89Ûªs", "It is", tweet)
    tweet = re.sub(r"Here\x89Ûªs", "Here is", tweet)
    tweet = re.sub(r"who's", "who is", tweet)
    tweet = re.sub(r"I\x89Ûªve", "I have", tweet)
    tweet = re.sub(r"y'all", "you all", tweet)
    tweet = re.sub(r"can\x89Ûªt", "cannot", tweet)
    tweet = re.sub(r"would've", "would have", tweet)
    tweet = re.sub(r"it'll", "it will", tweet)
    tweet = re.sub(r"we'll", "we will", tweet)
    tweet = re.sub(r"wouldn\x89Ûªt", "would not", tweet)
    tweet = re.sub(r"We've", "We have", tweet)
    tweet = re.sub(r"he'll", "he will", tweet)
    tweet = re.sub(r"Y'all", "You all", tweet)
    tweet = re.sub(r"Weren't", "Were not", tweet)
    tweet = re.sub(r"Didn't", "Did not", tweet)
    tweet = re.sub(r"they'll", "they will", tweet)
    tweet = re.sub(r"they'd", "they would", tweet)
    tweet = re.sub(r"DON'T", "DO NOT", tweet)
    tweet = re.sub(r"That\x89Ûªs", "That is", tweet)
    tweet = re.sub(r"they've", "they have", tweet)
    tweet = re.sub(r"i'd", "I would", tweet)
    tweet = re.sub(r"should've", "should have", tweet)
    tweet = re.sub(r"You\x89Ûªre", "You are", tweet)
    tweet = re.sub(r"where's", "where is", tweet)
    tweet = re.sub(r"Don\x89Ûªt", "Do not", tweet)
    tweet = re.sub(r"we'd", "we would", tweet)
    tweet = re.sub(r"i'll", "I will", tweet)
    tweet = re.sub(r"weren't", "were not", tweet)
    tweet = re.sub(r"They're", "They are", tweet)
    tweet = re.sub(r"Can\x89Ûªt", "Cannot", tweet)
    tweet = re.sub(r"you\x89Ûªll", "you will", tweet)
    tweet = re.sub(r"I\x89Ûªd", "I would", tweet)
    tweet = re.sub(r"let's", "let us", tweet)
    tweet = re.sub(r"it's", "it is", tweet)
    tweet = re.sub(r"can't", "cannot", tweet)
    tweet = re.sub(r"don't", "do not", tweet)
    tweet = re.sub(r"you're", "you are", tweet)
    tweet = re.sub(r"i've", "I have", tweet)
    tweet = re.sub(r"that's", "that is", tweet)
    tweet = re.sub(r"i'll", "I will", tweet)
    tweet = re.sub(r"doesn't", "does not", tweet)
    tweet = re.sub(r"i'd", "I would", tweet)
    tweet = re.sub(r"didn't", "did not", tweet)
    tweet = re.sub(r"ain't", "am not", tweet)
    tweet = re.sub(r"you'll", "you will", tweet)
    tweet = re.sub(r"I've", "I have", tweet)
    tweet = re.sub(r"Don't", "do not", tweet)
    tweet = re.sub(r"I'll", "I will", tweet)
    tweet = re.sub(r"I'd", "I would", tweet)
    tweet = re.sub(r"Let's", "Let us", tweet)
    tweet = re.sub(r"you'd", "You would", tweet)
    tweet = re.sub(r"It's", "It is", tweet)
    tweet = re.sub(r"Ain't", "am not", tweet)
    tweet = re.sub(r"Haven't", "Have not", tweet)
    tweet = re.sub(r"Could've", "Could have", tweet)
    tweet = re.sub(r"youve", "you have", tweet)  
    tweet = re.sub(r"donå«t", "do not", tweet)        
    # Character entity references
    tweet = re.sub(r"&amp;", "&", tweet)
    tweet = tweet.lower().replace('[^\w\s]',' ').replace('\s\s+', ' ')
    tweet = str(tweet)
    stemmer = PorterStemmer()
    # stopwords_english = nltk.download('stopwords').words('english')
    stopwords_english = set(nltk.corpus.stopwords.words('english'))

    # remove stock market tickers like $GE
    tweet = re.sub(r'\$\w*', '', tweet)

    # remove old style retweet text "RT"
    tweet = re.sub(r'^RT[\s]+', '', tweet)

    # remove hyperlinks
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)

    # remove hashtags
    # only removing the hash # sign from the word
    tweet = re.sub(r'#', '', tweet)

    # tokenize tweets
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    tweet_tokens = tokenizer.tokenize(tweet)

    tweets_clean = []
    for word in tweet_tokens:
        if (word not in stopwords_english and word not in string.punctuation):
            stem_word = stemmer.stem(word)
            tweets_clean.append(stem_word)
    
    clean_tweet = ' '.join(map(str, tweets_clean))
    return clean_tweet

def sarcasm_model(raw_input):
    with open('Models/sarcasm_model/tokenizer_s.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    tw = tokenizer.texts_to_sequences([raw_input]) #test_word
    tw = pad_sequences(tw,maxlen=200)
    with open('Models/sarcasm_model/model_s.json', 'r') as f: 
        json = f.read() 
    f.close()
    loaded_model = model_from_json(json)
    loaded_model.load_weights("Models/sarcasm_model/model_s.h5")
    output = loaded_model.predict(tw)
    return output[0][0]

def twitter_model(raw_input):
    clean_tweet = preprocess_tweet(raw_input)
    sarc_op = sarcasm_model(clean_tweet)
    with open('Models/twitter_model/tokenizer_t.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    tw = tokenizer.texts_to_sequences([clean_tweet]) #test_word
    tw = pad_sequences(tw,maxlen=200)
    with open('Models/twitter_model/model_t.json', 'r') as f: 
        json = f.read() 
    f.close()
    loaded_model = model_from_json(json)
    loaded_model.load_weights("Models/twitter_model/model_t.h5")
    output = loaded_model.predict(tw)
    return output[0][0], sarc_op

def reddit_model(raw_input):
    loaded_model = load_model("Models/reddit_model", custom_objects={"KerasLayer": hub.KerasLayer}, compile=False)
    output = loaded_model.predict([raw_input])
    return output[0][0]

def twitter_scrape():
    consumer_key = '1ljbylLYSgk6FIpepCzhQVKUE'
    consumer_secret = 'WGIsKEobyGx2FbS3uvZfVMeFAOwMmusvGCTqjuSnqbU7TQI4N3'
    access_token = '839721048538914817-01LEnkpGcjdDXL8grKxJ8r7UvrkVqQ6'
    access_token_secret = 'GgByKXcBqQoW0G3sz4clhNWryOWCKKHzFkVn0yscHSkej'
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    search_words = ["suicide","suicidal","selfharm","hatemyself","iwanttodie", "cutmyself", "ptsd"]
    tweetstore = []
    userid = []
    username = []
    created = []
    platform = []
    for search_word in search_words:
        # Collect tweets
        tweets = tw.Cursor(api.search,
                    q=search_word,
                    lang="en").items(10)
        # Collect a list of tweets
        for tweet in tweets:
            tweetstore.append(tweet.text) 
            userid.append(tweet.user.id)
            username.append(tweet.user.name)
            created.append(tweet.created_at)
            platform.append("twitter")
    df = pd.DataFrame({"userid": userid, "username": username, "post": tweetstore, "created": created, "platform": platform})
    return df

def reddit_scrape():
    reddit = praw.Reddit(client_id='uycdldw7XT9KNA', client_secret='mdW0O0OD7np6UpM67VVCozeUvdEPvw', user_agent='Reddit webscrapping')
    all_subreddit = reddit.subreddit('SuicideWatch+depression+selharm').hot(limit=10)
    reddits = []
    userid = []
    created = []
    username = []
    platform = []
    for post in all_subreddit:
        reddits.append(post.selftext)
        if post.author:
            userid.append(post.author.id)
            username.append(post.author.name)
        else:
            userid.append('NA')
            username.append('NA')
        created.append(datetime.fromtimestamp(int(post.created_utc)))
        platform.append("reddit")
    df = pd.DataFrame({"userid": userid, "username": username, "post": reddits, "created": created, "platform": platform})
    return df


