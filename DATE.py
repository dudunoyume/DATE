import os
import numpy as np
import pandas as pd
import str


class DAT(object):

    def __init__(self, path):
        self.path = path

    def inp(self, path):
        global dfold
        dfold = pd.read_excel(path, header=1, sheet_name=1)
        datlist = dfold["日期"]
        return datlist

    def pickup(self, datlist):
        iconlist = [".", ",", "/", "-"]
        for i in datlist:
            if "." in i:
                str1 = i.split(".")
            elif "." in i:
                str1 = i.split(".")


a = "2020-1-2"
print(a.split['-'])
print(b)
iconlist = [".", ",", "/", "-"]
iconlist in b
