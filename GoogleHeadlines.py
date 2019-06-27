# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 20:34:51 2018

@author: Kushal / Hillel
"""
from flask import Flask
from flask import render_template
from bs4 import BeautifulSoup as soup
from textblob import TextBlob
import sys


if sys.version_info >= (3,):
    import urllib.request as urllib2
else:
    import urllib2

app = Flask(__name__)

@app.route('/')
def google_headlines():
    news_url = "https://news.google.com/news/rss/"
    Client = urllib2.urlopen(news_url)
    xml_page=Client.read()
    Client.close()
    soup_page=soup(xml_page,'xml')
    news_list=soup_page.findAll('item')
    positive = 0
    negative = 0
    neutral = 0
    polarity = 0
    headlines_sentiment = ("Positive =" + str(positive) + "negative =" + str(negative) + "neutral =" + str(neutral))
    # Print news title, url and publish date
    for news in news_list:
      print(news.title.text)
      print(news.link.text)
      print(news.pubDate.text)
      headline = str(news.title.text)
      newstime = str(news.pubDate.text)
      print("-"*60)
      analysis = TextBlob(news.title.text)
      polarity += analysis.sentiment.polarity
      if (analysis.sentiment.polarity == 0):
          neutral += 1
      elif (analysis.sentiment.polarity < 0):
           negative += 1
      elif (analysis.sentiment.polarity > 0):
           positive += 1
      positive = format(positive, '.1f')
      negative = format(negative, '.1f')
      neutral = format(neutral, '.1f')
      headlines_sentiment = ("Positive =" + str(positive) + "negative =" + str(negative) + "neutral =" + str(neutral))
      print("Positive =" + positive + "negative =" + negative + "neutral =" + neutral)
      positive = 0
      negative = 0
      neutral = 0
      polarity = 0
      return render_template('index.html')
      #return headline, headlines_sentiment, newstime;


#positive = sum(positive, news.title.text)
#negative = sum(negative, news.title.text)
#neutral = sum(neutral, news.title.text)

  # format the below to 2 decimal places

if __name__ == '__main__':
    app.run(debug='true');
    #app.run(host='192.168.1.1',port='5000');
