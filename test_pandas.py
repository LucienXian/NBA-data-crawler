import pandas as pd


# Create a Pandas dataframe from some data.
df = pd.DataFrame({'序号': [10, 20, 30, 20, 15, 30, 45],
                    '球队': [0, 0, 0, 0, 5, 0, 5]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()