#coding=utf-8
import requests
import time
import urllib
from bs4 import BeautifulSoup
import re
import pandas as pd

TEAM_INFO_CON = ['球员','出场','时间','投篮','命中','出手','三分','命中','出手','罚球','命中','出手',
                '篮板','前场','后场','助攻','抢断','盖帽','失误','犯规','得分']

TEAM_NAME_TO_YEAR = {'ATL':1968, 'CHI':1966,'BKN':2012,'CHA':2004,'CLE':1970,'BOS':1946,'MIA':1988,
                    'DET':1957,'NYK':1946,'ORL':1989,'IND':1976,'PHI':1963,'WAS':1997,'MIL':1968,
                    'TOR':1995,'GSW':1971,'DEN':1976,'DAL':1980,'LAC':1984,'MIN':1989,'HOU':1971,
                    'LAL':1960,'OKC':2008,'MEM':2001,'PHO':1968,'POR':1970,'NOH':2002,'SAC':1985,
                    'UTA':1979,'SAS':1976}


def getNBASingleData(url):
    # url = 'view-source:http://stat-nba.com/team/stat_box_team.php?team=GSW&season=2017&col=pts&order=1&isseason=1'
    # html = requests.get(url).text
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)
    if soup.find('tbody') is None:
        return None
    data = soup.find('tbody').text
    list_data = data.split('\n')
    return list_data

def getNBAAllData(url):
    datasets = ['']
    data1 = getNBASingleData(url)
    if data1 is None:
        return None
    datasets.extend(data1)
    #去掉数据里的空元素
    for item in datasets[:]:
        if len(item) == 0:
            datasets.remove(item)
    return datasets

def constructURLTail(url_tail, year, name):
    return url_tail % (name, year)

def saveDataToExcel(datasets,sheetname, writer):
    df = pd.DataFrame(columns=TEAM_INFO_CON)
 
    num = 21
    row_cnt = 0
    data_cnt = 0
    data_len = len(datasets)
    print('data_len:',data_len)
    flag = False
    if data_len % num != 0:
        rows = (data_len-3)/num
        flag = True
    while(data_cnt< data_len):
        row_cnt += 1
        print('序号:',row_cnt)
        if flag and row_cnt > rows-3:
            break
        row = []
        for col in range(num):
            row.append(datasets[data_cnt])
            data_cnt += 1
        df.loc[row_cnt] = row

    df.to_excel(writer, sheet_name=sheetname)

if __name__ == "__main__":
 
    
    #url_header = 'http://stat-nba.com/team/stat_box_team.php?team='
    
    for name, year in TEAM_NAME_TO_YEAR.items():
        sheet_num = 2018-year
        filename = 'nba_team_reg_data('+name+').xlsx'

        writer = pd.ExcelWriter(filename)
        print(name)
        for y in range(sheet_num):
            url_header = 'http://stat-nba.com/team/stat_box_team.php?team='
            url_tail = '%s&season=%d&col=pts&order=1&isseason=0'
            print(year+y)
            url_tail = constructURLTail(url_tail, year+y, name)
            url = url_header+url_tail
            datasets = getNBAAllData(url)
            if datasets is None:
                continue
            sheetname = 'regularseason_data %d' %(year+y)
            saveDataToExcel(datasets, sheetname, writer)
        
        writer.save()