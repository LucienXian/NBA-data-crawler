import pandas as pd


xls = pd.ExcelFile('team_info.xlsx')
#team_info为表单名，要注意一个文件可能有多个表单
#注意，需要打开excel文件查看表单名，或者使用pandas提供的xls.sheet_names查看所有表单名
df1 = pd.read_excel(xls, 'team_info')

for row in range(df1.shape[0]): 
    for col in range(df1.shape[1]):
        print(df1.iat[row,col])
    print('---------------------------------------------------')
        