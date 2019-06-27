import sys
import re
import  os
import httplib2
from textblob import TextBlob
from bs4 import SoupStrainer
from requests import get
if sys.version_info >= (3,):
    import urllib.request as urllib2

else:
    import urllib2

#import the Beautiful soup functions to parse the data returned from the chosen website
from bs4 import BeautifulSoup
html = urllib2.urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
print(urllib2.HTTPError)
if html is None:
        print("URL is not found")
bsObj = BeautifulSoup(html.read(),'lxml');
print(bsObj.h1);
#This is the url that will be queried. You can change this to something else
#Of course if it is changed so will the structure of the returned html
#Hence the parse logic will beed to be modified
#urlStr = "https://epaperlive.timesgroup.com/ETE/BOM/20180623"
#Querying the website and returning the html to 'page'
#page = urllib2.urlopen("https://epaperlive.timesgroup.com/ETE/BOM/20180623")
#print(urllib2.HTTPError)
#if html is None:
#        print("URL is not found")
#page = requests.get(urlstr)
#print ("Querying = " + urlStr)
#Parsing the html in 'page', and storing it in Beautiful Soup format
#soup = BeautifulSoup(page.read(),'lxml')
#print(soup.text);
urlStr1 = "https://economictimes.indiatimes.com/archivelist/year-2018,month-6,starttime-43274.cms"
#page1 = urllib2.urlopen("https://economictimes.indiatimes.com/archivelist/year-2018,month-6,starttime-43274.cms")
hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Referer': 'https://cssspritegenerator.com',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}
print(urllib2.HTTPError)
if html is None:
        print("URL is not found")
#page = requests.get(urlstr)
page1=get(urlStr1,headers=hdr)
soup1 = BeautifulSoup(page1.text, 'html.parser', parse_only=SoupStrainer('a'))
#data = soup1.find('div', {'class' : 'content'})
print ("Querying = " + urlStr1)
#news_field= BeautifulSoup(news_data, 'lxml')
if soup1.attrs == 'href':
    print(soup1.prettify());
#print(soup1.prettify());
news_list = soup1.get_text('\n').replace('\n','\n\n')
line= len(news_list.split('\n\n'))
print(line)
#print(news_list)
news_word = "Reliance"
news_data = open('C:/Users/khushal/Documents/Python Scripts/news.txt', 'w+',encoding="utf-8")
if news_data == "Error":
    sys.exit("Error in Getting Date File : Stop Processing")
news_data.write(str(news_list));
news_data_txt = open('C:/Users/khushal/Documents/Python Scripts//news.txt', 'r',encoding="utf-8")
positive = 0
negative = 0
neutral = 0
polarity = 0
for line in news_data_txt:
    if news_word in line:
        print("-" * 60)
        print(line)
        analysis = TextBlob(line)
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
        print("Positive =" + positive + "negative =" + negative + "neutral =" + neutral)
        positive = 0
        negative = 0
        neutral = 0
        polarity = 0
news_data.close();
#news_data_txt = open('C:/Users/khushal/Downloads/Python stuff/BSEmain/news.txt', 'r',encoding="utf-8")

#a = re.compile(r'\b({0})\b'.format(news_word), flags=re.IGNORECASE).search(news_list,0,line )
#a= nparse.extract_test_sentences(news_list,news_word)
#a= ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\ / \ / \S+)", " ", news_list).split('\n\n'))
#print(a)
#print(news_list);
#http = httplib2.Http()
#status, response = http.request('https://economictimes.indiatimes.com')
#link= BeautifulSoup(response,'lxml', parse_only=SoupStrainer('a'))
#if link.has_attr('href'):
#    print(link['href'])

