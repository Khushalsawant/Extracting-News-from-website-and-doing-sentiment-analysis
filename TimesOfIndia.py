from lxml import etree
import sys
from requests import get
import requests
import pandas as pd
from bs4 import BeautifulSoup
from lxml import html
import html5lib
from io import StringIO, BytesIO
if sys.version_info >= (3,):
    import urllib.request as urllib2
else:
    import urllib2


url = 'https://www.screener.in/company/RELIANCE/'
parser = etree.HTMLParser()
tree = etree.parse(StringIO(url),parser)
result = etree.tostring(tree.getroot(),pretty_print=True, method="html")
#tree = html.parse(web)
#res = requests.get(url)
#doc = html.parse(base_url=url)
#.content,parser='lxml.etree._BaseParser')
print(result)
web = urllib2.urlopen("https://www.screener.in/company/RELIANCE/")
hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Referer': 'https://cssspritegenerator.com',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}
print(urllib2.HTTPError)
page1= get(web,headers=hdr)
#soup = BeautifulSoup(page1.text,"lxml",'html.parser',parse_only=SoupStrainer('table'))
#table = soup.find("table", attrs={"class":"details"})
# The first tr contains the field names.
soup = BeautifulSoup(page1.text,'lxml', 'html.parser')
table = soup.find("table")

# The first tr contains the field names.
headings = [th.get_text().strip() for th in table.find("tr").find_all("th")]

print(headings)

datasets = []
for row in table.find_all("tr")[1:]:
    dataset = dict(zip(headings, (td.get_text() for td in row.find_all("td"))))
    datasets.append(dataset)

print(datasets)