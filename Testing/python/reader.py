import pandas as pd

#Not gonna lie idk where this file is supposed to be in the directory
#And i cant figure out how to import models from here

xls = pd.ExcelFile("../excel files/Batch 2023.xlsx")
df_Fees = pd.read_excel(xls, "Fees")
df_s1 = pd.read_excel(xls, "11 - A")
df_s2 = pd.read_excel(xls, "11 - B")
df_s3 = pd.read_excel(xls, "11 - C")
print(df_s1.head()) 

