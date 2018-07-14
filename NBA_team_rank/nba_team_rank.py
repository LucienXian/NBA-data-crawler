#coding=utf-8
import requests
import time
import urllib
from bs4 import BeautifulSoup
import re
import pandas as pd

TEAM_INFO_CON = ('东部','胜','负','胜率','胜场差','主教练')

def getNBASingleData(url):
    # url = 'stat-nba.com/wper/2017.html'
    # html = requests.get(url).text
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)
    tables = soup.findAll("table")
    list_data = []
    flag = False
    for tr in tables[1].findAll('tr'):
        if not flag:
            flag = True
            continue
        for th in tr.findAll('td'):
            list_data.append(th.text)
    #list_data = data.split('\n')
    return list_data

def getNBAAllData(url):
    datasets = ['']
    data1 = getNBASingleData(url)
    #print(data1)
    datasets.extend(data1)
    #去掉数据里的空元素
    for item in datasets[:]:
        if len(item) == 0:
            datasets.remove(item)
    return datasets

def saveDataToExcel(datasets,sheetname, writer):
    df = pd.DataFrame(columns=TEAM_INFO_CON)
 
    num = 6
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
    startYear = 1985
    yearNum = 2018-startYear
    url = 'http://stat-nba.com/wper/%d.html'
    #filename = 'nba_rank_data_east.xlsx'
    filename = 'nba_rank_data_west.xlsx'
    writer = pd.ExcelWriter(filename)
    for year in range(yearNum):
        url_ = url % startYear
        #print(url)
        datasets = getNBAAllData(url_)
        sheetname = 'west_rank_data %d' %(startYear)
        saveDataToExcel(datasets, sheetname, writer)
        startYear+=1
    writer.save()
        