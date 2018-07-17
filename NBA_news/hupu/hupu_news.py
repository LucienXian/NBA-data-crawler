import requests
import time
import urllib
from bs4 import BeautifulSoup
import re
import json

URL_TO_TEAM = {2982:'勇士',3023:'骑士',811:'火箭',2994:'马刺',
                2987:'雷霆',2698:'热火',3020:'凯尔特人',2990:'森林狼',
                2985:'老鹰',2700:'尼克斯',3027:'太阳',3008:'开拓者',
                3021:'鹈鹕',3034:'国王',3033:'魔术',3022:'篮网',
                2984:'快船',3019:'黄蜂',3024:'独行侠',2978:'公牛',
                3036:'奇才',821:'活塞',3035:'猛龙',2992:'76人',
                3029:'灰熊',2997:'爵士',3030:'雄鹿',3025:'掘金'}

PAGES = 30
TEAM = '%s %s队'

def getContents(url):
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.error.URLError:
        print("Bad URL or timeout")
        return None, None
    soup = BeautifulSoup(html)
    content_div = soup.find('div',{'class':'artical-main-content'})
    if not content_div:
        return None, None
    content = ''
    for p in content_div.findAll('p'):
        content += p.text
    time_div = soup.find('span', {'id':'pubtime_baidu'})
    if not time_div:
        return None
    time = time_div.text.strip()
    print(time)
    print(content)
    return content, time


def getNBAAllData(url, label):
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.error.URLError:
        print("Bad URL or timeout")
        return []
    soup = BeautifulSoup(html)
    data = []
    for news in soup.findAll('div', {'class':'list-content'}):
        a = news.find('a', href=True)
        if not a:
            return []
        title = a.text
        print(title)
        url = a['href']
        print(url)
        print(label)
        contents, time = getContents(url)
        data.append({'title':title, 'time':time, 'url':url, 'content': contents, 'label':label})
        print('---------------------------------')
    return data

        



if __name__ == "__main__":
    url = "https://voice.hupu.com/nba/tag/%d-%d.html"
    filename = 'hupu.json'
    list_data = []
    for u, team in URL_TO_TEAM.items():
        for page in range(1, PAGES+1, 2):
            url_ = url % (u, page)
            t = TEAM % (team, team)
            print('go to ' + url_)
            datasets = getNBAAllData(url_, t)
            list_data.extend(datasets)
    with open(filename, 'w+') as json_file:
        jsoned_data = json.dumps(list_data, indent=4)
        json_file.write(jsoned_data)