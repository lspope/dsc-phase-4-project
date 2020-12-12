from nltk.corpus import stopwords
from nltk import word_tokenize, FreqDist
from nltk.tokenize import TweetTokenizer
from nltk.stem import WordNetLemmatizer

import string
import re
import wordcloud

import pandas as pd
import numpy as np
from PIL import Image
from os import path

from sklearn.metrics import accuracy_score, plot_confusion_matrix, plot_confusion_matrix, classification_report

import matplotlib.pyplot as plt
import matplotlib.colors
import seaborn as sns


lemmatizer = WordNetLemmatizer()

def get_eng_stopwords_list():
    # Get English stopwords, punctuation, and 'empty text' signifiers (like empty quotes and ...)
    return stopwords.words('english')  + list(string.punctuation) + ["''", '""', '...', '``']


def get_social_media_stopwords_list():
    return stopwords.words('english') + ['rt', 'link','&', 'SXSW', 'sxsw', 'austin'] + list(string.punctuation) + ["''", '""', '..', '...', '``']


def clean_tweet(tweet):
    # remove hashtags - only removing the hash # sign from the word
    tweet = re.sub(r'#', '', tweet)

    # remove hyperlinks
    # to remove links that start with HTTP/HTTPS in the tweet
    alt_url_regex =  'https?:\/\/(www\.)?[-a-zA-Z0–9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0–9@:%_\+.~#?&//=]*)'
    url_regex = '(?:<\w+.*?>|[^=!:\'\"/]|^)((?:https?://|www\.)[-\w]+(?:\.[-\w]+)*(?::\d+)?(?:/(?:(?:[~\w\+%-]|(?:[,.;@:][^\s$]))+)?)*(?:\?[\w\+%&=.;:-]+)?(?:\#[\w\-\.]*)?)(?:\p{P}|\s|<|$)'
    
    tweet = re.sub(r'https?:\/\/(www\.)?[-a-zA-Z0–9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0–9@:%_\+.~#?&//=]*)', '', tweet, flags=re.MULTILINE)

    # to remove other url links
    tweet = re.sub(r'[-a-zA-Z0–9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0–9@:%_\+.~#?&//=]*)', '', tweet, flags=re.MULTILINE) 
    
    return tweet


def tokenize_lemmatize_tweet(tweet):
    tweet_tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    tokens = tweet_tokenizer.tokenize(tweet)
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens


def tokenize_tweet(tweet):
    tweet_tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    tokens = tweet_tokenizer.tokenize(tweet)
    return tokens
    

def process_tweet_text_encode_to_ascii(tweet, stopwords_list):
    #tokenize, lowercase each token, remove stopwords
    stopwords_removed = ''
    tweet = clean_tweet(tweet)
    tweet_tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    try:
        tweet_encode = tweet.encode("ascii", "ignore")
        tweet_decode = tweet_encode.decode()
        tokens = tweet_tokenizer.tokenize(tweet_decode)
        stopwords_removed = [token for token in tokens if token not in stopwords_list]
    except:
        print('Could not encode/decode ', tweet )
    return stopwords_removed


def plot_word_cloud(text, word_max, stopwords_list, bg_color='black'):
    cloud = wordcloud.WordCloud(background_color=bg_color, 
                            min_word_length=2,
                            max_words=word_max)
    cloud.generate(text)
    
    # plot it
    plt.figure(figsize=(15,10))
    plt.imshow(cloud, interpolation='bilinear') 
    plt.axis("off")
    plt.show()


def show_peformance_metrics(y_train, y_train_pred, X_test, y_test, y_pred, names):
    train_score = accuracy_score(y_train, y_train_pred)
    test_score = accuracy_score(y_test, y_pred)
    print('--------------------------------------------------------------------------')
    print("Training Accuracy: {:.4} \t\t Testing Accuracy: {:.4}".format(train_score, test_score))
    print('--------------------------------------------------------------------------')
    print(classification_report(y_test, y_pred, target_names=names))
    print('--------------------------------------------------------------------------')


def plot_pretty_cf(predictor, xtest, ytest, cmap='Blues', normalize='true', title=None):
    fig, ax = plt.subplots(figsize=(8, 8))
    plot_confusion_matrix(predictor, xtest, ytest, cmap=cmap, normalize=normalize, ax=ax)
    ax.set_title(title, size='large')
    ax.set_xlabel('Predicted Label', size='medium')
    ax.set_ylabel('True Label', size='medium')
    plt.show()
