# Automate Excel Sheet
# pip install pandas

import pandas as excel

# read excel file
df = excel.read_excel('excel.xlsx', sheet_name='Sheet1')

# Modify to read any type of excel file extension
# if file_extension == 'xlsx':
#     df = pd.read_excel(file.read(), engine='openpyxl')
# elif file_extension == 'xls':
#     df = pd.read_excel(file.read())
# elif file_extension == 'csv':
#     df = pd.read_csv(file.read())

# print dataframe
print(df)

# Read by column name
print(df['Age'])

# Read by row number
print(df['Salary'][1])

# Read by row and column number
print(df[0][1])

# Get total rows and columns
row, col = df.shape
print(row, col)

# read by cell
print(df.iat[1, 1])

# Write by cell
df.iat[1, 1] = 'New Value'

# Write by row 
df.loc[1, 'Salary'] = 'New Value'

# Write by column
df.loc[:, 'Salary'] = 'New Value'

# Append new row
df.loc[row+1] = ['New Value', 'New Value']

# Append new column
df.loc[:, col+1] = 'New Value'

# save to excel file
df.to_excel('excel.xlsx', sheet_name='Sheet1')