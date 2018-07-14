import requests
import time
import urllib
from bs4 import BeautifulSoup
import re
import pandas as pd

PLAYER_INFO_CON = ('全名','位置','身高','体重','出生年月','出生城市')
INFO_NUM = 6

def getNBASingleData():
    player_num = 4654
    #player_num = 1830
    url = 'http://stat-nba.com/player/%d.html'
    list_data = []
    for i in range(1, player_num):
        url_ = url % i
        if i == 1828 or i == 2276 or i==4079 or i==4420:
            continue
        print("crawl url:" + url_)
        try:
            html = urllib.request.urlopen(url_).read()
        except urllib.error.URLError:
            print("Bad URL or timeout")
            continue
        
        soup = BeautifulSoup(html)
        mydivs = soup.findAll("div", {"class": "detail"})
        
        for div in mydivs:
            num = INFO_NUM
            if len(div.findAll("div", {"class": "row"})) < num:
                print(len(div.findAll("div", {"class": "row"})))
                break
            for d in div.findAll("div", {"class": "row"}):
                num -= 1
                s = None
                s = d.text.split(':')[1]
                list_data.append(s)
                if num==0:
                    break
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
 
    num = INFO_NUM
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
        