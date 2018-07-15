import requests
import time
import urllib
from bs4 import BeautifulSoup
import re
import pandas as pd

SALARY_INFO = ('球员','薪资')
SEASON = 2017
TEAM_NAME_TO_YEAR = ['ATL', 'CHI','BKN','CHA','CLE','BOS','MIA',
                    'DET','NYK','ORL','IND','PHI','WAS','MIL',
                    'TOR','GSW','DEN','DAL','LAC','MIN','HOU',
                    'LAL','OKC','MEM','PHO','POR','NOH','SAC',
                    'UTA','SAS']

def getNBASingleData(url):
    # url = 'http://stat-nba.com/team/salary.php?name_eng_short=ATL&season=2017'
    # html = requests.get(url).text
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)
    data = soup.html.body.find('tbody').text
    list_data = data.split('\n')
    return list_data

def getNBAAllData(item):
    datasets = ['']
    data1 = getNBASingleData(item)
    datasets.extend(data1)
    #去掉数据里的空元素
    for item in datasets[:]:
        if len(item) == 0:
            datasets.remove(item)
    return datasets

def saveDataToExcel(datasets,sheetname, writer):
    df = pd.DataFrame(columns=SALARY_INFO)
 
    num = 2
    row_cnt = 0
    data_cnt = 0
    data_len = len(datasets)
    datasets = datasets[:(data_len-6)]
    print('data_len:',data_len - 6)
    while(data_cnt< data_len - 6):
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
    filename = 'NBA_team_salary '+str(SEASON)+'.xlsx'
    writer = pd.ExcelWriter(filename)
    url = 'http://stat-nba.com/team/salary.php?name_eng_short=%s&season=%d'
    for i, name in enumerate(TEAM_NAME_TO_YEAR):
        url_ = url % (name, SEASON)
        sheetname = 'salary team %s' %(name)
        datasets = getNBAAllData(url_)
        saveDataToExcel(datasets, sheetname, writer)
    writer.save()

