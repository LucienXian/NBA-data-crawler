import requests
import time
import urllib
from bs4 import BeautifulSoup
import re
import json

TEAM = ['rocketsgd2016','cavaliersgd2016','warriorsgd2016','celticsnews','okcgd2016',
        'lakersgd2016','spursgd2016']

def getContents(url):
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.error.URLError:
        print("Bad URL or timeout")
        return 'None'
    soup = BeautifulSoup(html, fromEncoding="gb18030")
    text_ = soup.find('div',{'class':'post_text'})
    if text_:
        contents = text_.text
    else:
        return None
    print(contents)
    return contents

def getPageUrls(url):
    urllist = []
    for i in range(1, 21):
        if i == 1:
            urllist.append(url)
        elif i<10:
            urllist.append(url[:-1]+'_0%d' %(i))
        else:
            urllist.append(url[:-1]+'_%d' %(i))
    return urllist

def getPagesAndurls(url, soup):
    pageDiv = soup.find("div", {"class": "news_page clearfix"})
    pageNum = 0
    urls = []
    for li in pageDiv.findAll("li")[2:-2]:
        pageNum += 1
        if li.find('a', href=True):
            urls.append(li.find('a')['href'])
    print(pageNum)
    #print(urls)
    return pageNum, urls

def getNBAAllData(url):
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.error.URLError:
        print("Bad URL or timeout")
        return []
    soup = BeautifulSoup(html)
    urls = getPageUrls(url)
    data = []
    for u in urls:
        try:
            print(u)
            html = urllib.request.urlopen(u).read()
            
        except urllib.error.URLError:
            print("Bad URL or timeout")
            continue
        soup = BeautifulSoup(html)
        news_items = soup.find_all('div', {'class':'news_item'})
        for item in news_items:
            title_ = item.find('h3')
            title = title_.text
            print(title)
            url = title_.find('a')['href']
            print(url)
            time = item.find('div', {'class':'post_date'}).text
            print(time)
            keywords_data = item.find('div', {'class':'keywords'}).text
            keywordlist = keywords_data.split('\n')
            keywords = ' '.join(keywordlist)
            print(keywords)
            contents = getContents(url)
            if not contents:
                continue
            data.append({'title':title, 'time':time, 'url':url, 'content': contents, 'label':keywords})
            print("----------------------------------")
    return data



if __name__ == "__main__":
    url = 'http://sports.163.com/special/%s/'

    filename = 'netease'
    data = []
    for team in TEAM:
        url_ = url % team
        print('go to ' + url_)
        datasets = getNBAAllData(url_)
        data.extend(datasets)
    with open(filename, 'w+') as json_file:
        jsoned_data = json.dumps(data, indent=4)
        json_file.write(jsoned_data)
