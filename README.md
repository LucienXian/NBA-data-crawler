# 该项目为相关nba数据的爬虫


在目录NBA\_team\_info/下有一个读取excel文件的脚本——**[test_read.py](https://github.com/LucienXian/NBA-data-crawler/blob/master/NBA_team_info/test_read.py)**
在主目录下有一个读取json文件的脚本——**[test_json.py](https://github.com/LucienXian/NBA-data-crawler/blob/master/test_json.py)**

## 第三方库

```shell
beautifulsoup4  4.6.0 
pandas          0.23.3
xlrd            1.1.0
```



## 球队



有些文件名用了球队代号作为区分，比如nba_team_reg_data(CHI).xlsw，就是公牛队的数据：

```python
{'ATL':老鹰, 'CHI':公牛,'BKN':篮网,'CHA':黄蜂,'CLE':骑士,'BOS':凯尔特人,'MIA':热火,
                    
 'DET':活塞,'NYK':尼克斯,'ORL':魔术,'IND':步行者,'PHI':76人,'WAS':奇才,'MIL':雄鹿,
                    
 'TOR':猛龙,'GSW':勇士,'DEN':掘金,'DAL':独行侠,'LAC':快船,'MIN':森林狼,'HOU':火箭,
                    
 'LAL':湖人,'OKC':雷霆,'MEM':灰熊,'PHO':太阳,'POR':开拓者,'NOH':鹈鹕,'SAC':国王,
 
 'UTA':爵士,'SAS':马刺}
```





* NBA_team_info

**team_info.xlsx**：球队的基本信息，字段如下：

| 中文队名 | 英文队名 | 所属地区 | 成立时间 | 主球馆 | 拥有者 | 赛区 | 主教练 | logo |
| :------: | :------: | :------: | :------: | :----: | :----: | :--: | :----: | :--: |
|   str    |   str    |   str    |   time   |  str   |  str   | str  |  str   | str  |



* NBA_seasons_reg

**nba_regularseason_data from 2009.xlsx**：常规赛的比赛统计数据，从2009年起，有多个表单，表单名为——**regularseason_data xxxx**（xxxx为年份），表单内有字段：

| 序号 | 球队 | 时间 |   结果   | 主客 | 比赛 | 投篮命中率 | 命中数 | 出手数 | 三分命中率 | 三分命中数 | 三分出手数 | 罚球命中率 | 罚球命中数 | 罚球出手数 | 篮板 | 前场篮板 | 后场篮板 | 助攻 | 抢断 | 盖帽 | 失误 | 犯规 | 得分 |
| :--: | :--: | :--: | :------: | :--: | :--: | :--------: | :----: | :----: | :--------: | :--------: | :--------: | :--------: | :--------: | :--------: | :--: | :------: | :------: | :--: | :--: | :--: | :--: | :--: | :--: |
| int  | str  | time | bool/str | str  | str  |    str     |  int   |  int   |    str     |    int     |    int     |    str     |    int     |    int     | int  |   int    |   int    | int  | int  | int  | int  | int  | int  |



* NBA_team_reg

文件夹下有若干个表。

**nba_team_reg_data(xxx).xlsw**(xxx为球队代号)：球队从成立到2018年的所有球员的**常规赛**相关数据，有若干个表单，表单名为**regularseason_data xxxx**(xxxx为年份)，表单内有字段：

| 球员 | 出场 | 首发 | 时间  | 投篮 | 命中  | 出手  | 三分 | 命中  | 出手  | 罚球 | 命中  | 出手  | 篮板  | 前场  | 后场  | 助攻  | 抢断  | 盖帽  | 失误  | 犯规  | 得分  |
| :--: | :--: | :--: | :---: | :--: | :---: | :---: | :--: | :---: | :---: | :--: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| str  | int  | int  | float | str  | float | float | str  | float | float | str  | float | float | float | float | float | float | float | float | float | float | float |



* NBA_team_playoff

文件夹下有若干个表。

**nba_team_reg_data(xxx).xlsw**(xxx为球队代号)：球队从成立到2018年的所有球员的**季后赛**相关数据，有若干个表单，表单名为**regularseason_data xxxx**(xxxx为年份)，表单内有字段：

| 球员 | 出场 | 首发 | 时间  | 投篮 | 命中  | 出手  | 三分 | 命中  | 出手  | 罚球 | 命中  | 出手  | 篮板  | 前场  | 后场  | 助攻  | 抢断  | 盖帽  | 失误  | 犯规  | 得分  |
| :--: | :--: | :--: | :---: | :--: | :---: | :---: | :--: | :---: | :---: | :--: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| str  | int  | int  | float | str  | float | float | str  | float | float | str  | float | float | float | float | float | float | float | float | float | float | float |



* NBA_team_rank

**nba_rank_data_east.xlsw**和**nba_rank_data_west.xlsx**，分别为从1985年开始的球队排名。每个文件有若干个表单——**east_rank_data xxxx**（xxxx为年份）。字段：

| 东部 |  胜  |  负  | 胜率  | 胜场差 | 主教练 |
| :--: | :--: | :--: | :---: | :----: | :----: |
| str  | int  | int  | float | float  |  str   |



| 西部 |  胜  |  负  | 胜率  | 胜场差 | 主教练 |
| :--: | :--: | :--: | :---: | :----: | :----: |
| str  | int  | int  | float | float  |  str   |



## 球员

* NBA_player

大约4000位NBA球员的基本信息，字段如下：

| 英文名 | 位置 |   身高    |   体重    | 出生年月 | 出生城市 | 中文名 | 图片链接 |
| :----: | :--: | :-------: | :-------: | :------: | :------: | :----: | :------: |
|  str   | str  | str/float | str/float |   str    |   str    |  str   |   str    |

> 其中身高和体重分别有两种单位：米和n尺m寸，公斤和磅



## 薪酬

* NBA_team_salary

爬取的是当前赛季的数据，以万美元为单位，每个表中有一个球队的薪酬

| 球员 | 薪酬 |
| :--: | :--: |
| str  | int  |



## 新闻

目前的新闻来源有：新浪(sina)、网易(netease)、搜狐(sohu)、虎扑(hupu)

新闻以json存储，只有4个字段：

| 时间 | 内容 | 标题 | 标签 | 链接 |
| :--: | :--: | :--: | :--: | :--: |
| time | str  | str  | str  | str  |

