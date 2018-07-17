import requests
import time
import urllib
from bs4 import BeautifulSoup
import re
import pandas as pd

PLAYER_INFO_CON = ('英文名','位置','身高','体重','出生年月','出生城市','中文名','图片链接')
INFO_NUM = 6
EXP_NUM = [145, 509,519,1828, 2276, 4079, 4420]
IMG_URL = "http://stat-nba.com%s"
DEFAULT_URL = "http://stat-nba.com/image/playerImage/img_middle_common.jpg"

def getNBASingleData():
    player_num = 4654
    #player_num = 1830
    url = 'http://stat-nba.com/player/%d.html'
    list_data = []
    for i in range(1, player_num):
        url_ = url % i
        if i in EXP_NUM:
            continue
        print("crawl url:" + url_)
        try:
            html = urllib.request.urlopen(url_).read()
        except urllib.error.URLError:
            print("Bad URL or timeout")
            continue
        
        soup = BeautifulSoup(html)
        mydivs = soup.findAll("div", {"class": "detail"})
        title = soup.find('title')
        name_idx = title.text.find('/')
        if name_idx == -1:
            continue
        chinese_name = title.text[:name_idx]
        print(chinese_name)

        img_url = DEFAULT_URL
        img_div = soup.find('div', {'class':'image'})
        if not img_div:
            img_url = DEFAULT_URL
        else:
            img_src = img_div.find('img', src=True)
            if not img_src:
                img_url = DEFAULT_URL
            else:
                img_url = IMG_URL % (img_src['src'])
        print(img_url)      

        for div in mydivs:
            num = INFO_NUM
            if len(div.findAll("div", {"class": "row"})) < num:
                print(len(div.findAll("div", {"class": "row"})))
                break
            
            for d in div.findAll("div", {"class": "row"}):
                num -= 1
                s = None
                s = d.text.split(':')[1]
                print(s)
                list_data.append(s)
                if num==0:
                    break
            list_data.append(chinese_name)
            list_data.append(img_url)
            print('....', num)
    return list_data

def getNBAAllData():
    datasets = ['']
    data1 = getNBASingleData()
    #print(data1)
    datasets.extend(data1)
    #去掉数据里的空元素
    for item in datasets[:]:
        if len(item) == 0:
            datasets.remove(item)
    return datasets

def saveDataToExcel(datasets,sheetname, writer):
    df = pd.DataFrame(columns=PLAYER_INFO_CON)
 
    num = INFO_NUM+2
    row_cnt = 0
    data_cnt = 0
    data_len = len(datasets)
    print('data_len:',data_len)
    while(data_cnt< data_len):
        row_cnt += 1
        print('序号:',row_cnt)
        row = []
        for col in range(num):
                # print col
                row.append(datasets[data_cnt])
                data_cnt += 1
        df.loc[row_cnt] = row

    df.to_excel(writer, sheet_name=sheetname)

if __name__ == "__main__":
    
    filename = 'nba_player_info.xlsx'
    writer = pd.ExcelWriter(filename)
    sheetname = 'player_info'
    datasets = getNBAAllData()
    saveDataToExcel(datasets, sheetname, writer)
    writer.save()
        