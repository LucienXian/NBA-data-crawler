# 该项目为相关nba数据的爬虫



## 球队

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

