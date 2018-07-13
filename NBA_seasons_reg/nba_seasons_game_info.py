#coding=utf-8
import requests
import time
import urllib
from bs4 import BeautifulSoup
import re
import pandas as pd

TEAM_INFO_CON = ('序号','球队','时间','结果','主客','比赛','投篮命中率','命中数',
            '出手数','三分命中率','三分命中数','三分出手数','罚球命中率','罚球命中数',
            '罚球出手数','篮板','前场篮板','后场篮板','助攻','抢断','盖帽',
            '失误','犯规','得分')

"""
获取所有页面的URL列表
"""
def getURLLists(url_header,url_tail,pages):
    url_lists = []
    url_0 = url_header+'0'+url_tail
    print(url_0)
    url_lists.append(url_0)
    for i in range(1,pages+1):
        url_temp = url_header+str(i)+url_tail
        url_lists.append(url_temp)
    return url_lists
 
"""
获取所有2017赛季NBA常规赛数据
"""
def getNBAAllData(url_lists):
    datasets = ['']
    for item in url_lists:
        data1 = getNBASingleData(item)
        datasets.extend(data1)
    #去掉数据里的空元素
    for item in datasets[:]:
        if len(item) == 0:
            datasets.remove(item)
    return datasets

"""
获取1个页面NBA常规赛数据
"""
def getNBASingleData(url):
    # url = 'http://stat-nba.com/query_team.php?QueryType=game&order=1&crtcol=date_out&GameType=season&PageNum=3000&Season0=2016&Season1=2017'
    # html = requests.get(url).text
    html = urllib.request.urlopen(url).read()
    # print html
    soup = BeautifulSoup(html)
    data = soup.html.body.find('tbody').text
    list_data = data.split('\n')
    return list_data

''' 
def saveDataToExcel(datasets,sheetname,filename):
 
    writer = pd.ExcelWriter(filename)
    df = pd.DataFrame(columns=TEAM_INFO_CON)
 
    num = 24
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

    writer.save()
'''

def saveDataToExcel(datasets,sheetname, writer):
    df = pd.DataFrame(columns=TEAM_INFO_CON)
 
    num = 24
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

    

def writeDataToTxt(datasets):
    fp = open('nba_data.txt','w')
    line_cnt = 1
    for i in range(len(datasets)-1):
        #球队名称对齐的操作：如果球队名字过短或者为76人队是 球队名字后面加两个table 否则加1个table
        if line_cnt % 24 == 2 and len(datasets[i]) < 5 or datasets[i] == u'费城76人':
            fp.write(datasets[i]+'\t\t')
        else:
            fp.write(datasets[i]+'\t')
        line_cnt += 1
        if line_cnt % 24 == 1:
            fp.write('\n')
    fp.close()

def constructURLTail(url_tail, year):
    return url_tail % (year, year+1)

def getPages(startYear):
    if startYear == 2011:
        pages = int(1980/150)
    elif startYear == 2012:
        pages = int(2058/150)
    else:
        pages = pages = int(2460/150)
    return pages

if __name__ == "__main__":
 
    
    #url_header = 'http://stat-nba.com/query_team.php?page='
    
    startYear = 2009
    filename = 'nba_regularseason_data from '+str(startYear)+'.xlsx'
    #saveDataToExcel(datasets,sheetname,filename)

    writer = pd.ExcelWriter(filename)
    for _ in range(9):
        pages = getPages(startYear)
        url_header = 'http://stat-nba.com/query_team.php?page='
        url_tail = '&QueryType=game&order=0&crtcol=date_out&GameType=season&PageNum=3000&Season0=%d&Season1=%d#label_show_result'
        url_tail = constructURLTail(url_tail, startYear)
        url_lists = getURLLists(url_header,url_tail,pages)
        datasets = getNBAAllData(url_lists)
        sheetname = 'regularseason_data %d' %(startYear)
        saveDataToExcel(datasets, sheetname, writer)
        startYear+=1
    writer.save()
 
