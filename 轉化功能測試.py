from tkinter.tix import InputOnly
from xml.sax import default_parser_list
import numpy as np
import pandas as pd
import re
import chardet
from datetime import datetime


df = pd.read_excel("D:\\Desktop\\date_test.xlsx", header=0, sheet_name=0)
df

df['real_date'] = pd.TimedeltaIndex(df['date'], unit='d') + datetime(1899, 12, 30)


for i in df["date"]:
    if int(i) == True:
        print("yes")
    
    else:
        print("ss")