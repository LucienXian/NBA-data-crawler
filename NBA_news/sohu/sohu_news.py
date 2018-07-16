import requests
import time
import urllib
from bs4 import BeautifulSoup
import re
import json

EXP = 'http//www.sohu.com/a/230856886_458722'

def getDetails(url):
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.error.URLError:
        print("Bad URL or timeout")
        return None, None, None
    except ValueError:
        return None, None, None
    soup = BeautifulSoup(html)

    time = ':00'
    time_span = soup.find('span', {'class':'time'})
    if not time_span:
        return None, None, None
    time = time_span.text + time

    label = None
    label_list = []
    label_span = soup.find('span', {'class':'tag'})
    if not label_span:
        return None, None, None
    for l in label_span.findAll('a'):
        label_list.append(l.text)
    label = ' '.join(label_list)
    print(label)

    article = soup.find('article',{'class':'article'})
    if not article:
        return None, None, None
    contents = ''
    for p in article.findAll('p')[2:-1]:
        contents += p.text
    print(contents[:-9])
    return time, label, contents[:-9]

def getNBAAllData(url):
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.error.URLError:
        print("Bad URL or timeout")
        return []
    soup = BeautifulSoup(html)
    div_news_items = soup.find("div", "f14list")
    if not div_news_items:
        return []
    ul_news_items = div_news_items.find("ul")
    #count = 0
    data = []
    for item in ul_news_items.findAll("li"):
        #count += 1
        a = item.find('a')
        if not a:
            continue
        title = a.text
        if title[0:2] == '组图' or title[0:3]=='高清图' or title[-3:]=='(图)':
            continue
        print(title)
        url = a["href"]
        print(url)
        time, label, contents = getDetails(url)
        if not time or not label or not contents:
            continue
        data.append({'title':title, 'time':time, 'url':url, 'content': contents, 'label':label})
        print('---------------------------------')
        print('---------------------------------')
    return data
        

if __name__ == '__main__':
    url1 = 'http://sports.sohu.com/nba_a.shtml'
    url_ = 'http://sports.sohu.com/nba_a_%d.shtml'

    filename = 'sohu.json'
    data = []
    count = 0
    for i in range(2104, 2004, -1):
        count += 1
        url = url1 if i == 2104 else url_ % (i)
        print('url is ' + url)
        datasets = getNBAAllData(url)
        data.extend(datasets)
        print("Done %d pages", count)
    with open(filename, 'w+') as json_file:
        jsoned_data = json.dumps(data, indent=4)
        json_file.write(jsoned_data)