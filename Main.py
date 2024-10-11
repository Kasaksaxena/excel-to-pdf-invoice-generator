import pandas as pd
# glob module is use to retrieve files or dic
#that matches a specipic pattern
import glob

filepaths=glob.glob("Invoices/*.xlsx")

for filepath in filepaths:
    df=pd.read_excel(filepath,sheet_name="Sheet 1")
    print(df)
    