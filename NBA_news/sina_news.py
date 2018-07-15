import requests
import time
import urllib
from bs4 import BeautifulSoup
import re
import json

WEB_ID = 15
YEAR = '2018-'
DIV = 2

def getContent(url):
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.error.URLError:
        print("Bad URL or timeout")
        return None
    soup = BeautifulSoup(html)
    divtext = soup.find("div", {"class": "article"})
    text = divtext.text

    label = ''
    divlabel = soup.find("div", {"class": "keywords"})
    if divlabel:
        for a in divlabel.findAll('a'):
        #print(a.text)
            label += a.text + ' '
    else:
        label = 'NBA'
    print(label)

    return text, label

def getNBAAllData(url):
    # url = 'http://sports.sina.com.cn/nba/1.shtml'
    # html = requests.get(url).text
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.error.URLError:
        print("Bad URL or timeout")
    # print html
    
    div_id = ''

    soup = BeautifulSoup(html)
    div = soup.find("div", {"id": "S_Cont_1%d" % DIV})
    
    times = []
    for time in div.findAll('span'):
        time_str = time.text.replace('/', '-')
        time_str = YEAR + time_str
        print(time_str)
        times.append(time_str)
    
    titles = []
    for title in div.findAll('a'):
        print(title.text)
        titles.append(title.text)
    
    contents = []
    labels = []
    urls = []
    for url in div.findAll('a', href=True):
        href = url['href']
        print(href)
        content, label = getContent(href)
        urls.append(href)
        contents.append(content)
        labels.append(label)
    
    print(len(times), len(titles), len(urls), len(contents), len(labels))
    if len(times) == len(titles) == len(urls) == len(contents)==len(labels):
        list_data = []
        for title, time, url, content, label in zip(titles, times, urls, contents, labels):
            list_data.append({'title':title, 'time':time, 'url':url, 'content': content, 'label':label})

        return list_data
    else:
        return []

def test(datasets):
    with open('sina.json', 'w+') as json_file:
        jsoned_data = json.dumps(datasets, indent=4)
        json_file.write(jsoned_data)
    with open('sina.json', 'r') as json_file:
        json_data = json.load(json_file)
        for key in json_data:
            print(key["title"])

if __name__ == "__main__":
    url = 'http://sports.sina.com.cn/nba/%d.shtml'
    
    if DIV == 1:
        filename = 'sina%d.json'
    else:
        filename = '%dsina.json'
    filename_ = filename % WEB_ID
    url_ = url % WEB_ID
    print(url_)
    datasets = getNBAAllData(url_)
    with open(filename_, 'w+') as json_file:
        jsoned_data = json.dumps(datasets, indent=4)
        json_file.write(jsoned_data)
    #test(datasets)