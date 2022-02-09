import os
from tkinter.tix import InputOnly
from xml.sax import default_parser_list
import numpy as np
import pandas as pd


class DATin(object):

    def __init__(self, path, colname):
        self._path = path
        self._colname = colname  # 日期的欄位
        self.dfold = pd.read_excel(self._path, header=0, sheet_name=0)

    def pickup(self):
        """取出日期列"""
        datlist = self.dfold[self._colname]
        iconlist = [".", ",", "/", "-"]  # 需要判別的符號
        datedf = pd.DataFrame(columns=['Year', 'Month', 'Day'])
        n = 0
        """ 先判別民國年OR西元年"""
        for i in datlist:
            YMD = ["0", "0", "0"]
            i = str(i)
            """前三個數字的大小來判斷"""
            if int(i[0:3]) < 180:
                """轉換民國年為西元年"""
                i = str(1911+int(i[0:3]))+i[3:]

            """轉換有無分割符號"""

            for j in iconlist:
                if j in i:
                    YMD = i.split(j)
                    """輸出日月年的"""
                    """若日月為個位數則加0"""
                    if len(YMD[1]) == 1:
                        YMD[1] = "0"+YMD[1]
                    if len(YMD[2]) == 1:
                        YMD[2] = "0"+YMD[2]

                    break

            if YMD[0] == "0":
                YMD[0] = i[0:4]
                # 先寫入年分後一字元長度判斷格式
                # 完整八碼
                if len(i) == 8:
                    YMD[1] = i[4:6]
                    YMD[2] = i[6:]
                # 僅六碼
                elif len(i) == 6:
                    YMD[1] = "0"+i[4]
                    YMD[2] = "0"+i[5]
                # 有七碼
                else:
                    if i[4] != "1":
                        YMD[1] = "0"+i[4]
                        YMD[2] = i[5:7]
                    else:
                        # 無法判別時加上error
                        YMD[1] = "error"+i[4]
                        YMD[2] = i[5:7]

            datedf.loc[n, ] = YMD

            n += 1
        # 輸出年月日的dataframe
        return datedf


def main():
    path = input("輸入路徑:")
    datechange = DATin(path, "日期")
    datechange.pickup()
    print(datechange.pickup())


if __name__ == '__main__':
    main()
