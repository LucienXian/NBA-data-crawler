import pandas as pd


xls = pd.ExcelFile('team_info.xlsx')
df1 = pd.read_excel(xls, 'team_info')

for row in range(df1.shape[0]): 
    for col in range(df1.shape[1]):
        print(df1.iat[row,col])
    print('---------------------------------------------------')
        