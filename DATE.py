import os
from tkinter.tix import InputOnly
from xml.sax import default_parser_list
import numpy as np
import pandas as pd
import re
import time


class DATin(object):

    def __init__(self, path, colname):
        self._path = path
        self._colname = colname  # 日期的欄位
        self.dfold = pd.read_excel(self._path, header=0, sheet_name=0)

    @property
    def path(self):
        return self._path

    @property
    def colname(self):
        return self._colname

    def df_origin(self):
        return self.dfold

    def pickup(self):
        """取出日期列"""
        datlist = self.dfold[self._colname]
        iconlist = r"[年月,/\-\.]"  # 用正則表達是，需要判別的符號
        datedf = pd.DataFrame(columns=['Year', 'Month', 'Day'])
        n = 0
        """ 先判別民國年OR西元年"""
        for i in datlist:
            YMD = ["", "", ""]
            i = str(i)
            """前兩個數字的大小來判斷"""
            if int(i[0:2]) < 17:
                """轉換百位民國年(100年後)為西元年"""
                i = str(1911+int(i[0:3]))+i[3:]

            elif int(i[0:2]) > 21:
                """轉換十位民國年(99年前)為西元年"""
                i = str(1911+int(i[0:2]))+i[2:]

            """判斷有無轉分割符號>>>>年月日,/\-."""
            if re.search(iconlist, i):
                i = re.sub(r"[日]", "", i)  # 先去除 日 避免造成多出的空格
                YMD = re.split(iconlist, i)
                if len(YMD) < 3:
                    YMD.append("")
                """輸出日月年的"""
                """若日月為個位數則加0"""
                if len(YMD[1]) == 1:
                    YMD[1] = "0"+YMD[1]
                if len(YMD[2]) == 1:
                    YMD[2] = "0"+YMD[2]

            if YMD[0] == "":
                YMD[0] = i[0:4]
                # 先寫入年分後一字元長度判斷格式
                # 完整八碼
                if len(i) == 8:
                    YMD[1] = i[4:6]
                    YMD[2] = i[6:]
                # 僅六碼
                elif len(i) == 6:
                    if int(i[4:6]) <= 12:
                        YMD[1] = i[4:6]
                    else:
                        YMD[1] = "0"+i[4]
                        YMD[2] = "0"+i[5]
                elif len(i) == 5:
                    YMD[1] = "0"+i[4]
                # 有七碼
                else:
                    if i[4] != "1":
                        YMD[1] = "0"+i[4]
                        YMD[2] = i[5:7]
                    else:
                        # 無法判別時加上error
                        YMD[1] = i[4:7]
                        YMD[2] = "error"

            datedf.loc[n, ] = YMD

            n += 1
        # 輸出年月日的dataframe
        return datedf


class DATout(object):
    def __init__(self, datadf, split_icon="", yearform="西元年"):
        self._split_icon = split_icon
        # 決定分隔符號
        self._yearform = yearform
        # 年份形式預設西元年
        self._datadf = datadf
        # DATin 輸入的日月年表格
        self.datelist = []

    def combine(self):
        for i in range(0, len(self._datadf)):
            # 若是民國年則轉換
            if self._yearform == "民國年":
                self._datadf.loc[i, "Year"] = str(
                    int(self._datadf.loc[i, "Year"])-1911)
                # 我們透過for迴圈一行來判斷說 x 是否有值 如果沒有則不加入到新的字串內

            if self._split_icon != "年月日":  # 判斷是否選擇年月日連接，若為一般符號，直接相連
                # 以 join 加 if 的判斷式，若  日  為空格 則不加入
                combinelist = self._split_icon.join(
                    t for t in self._datadf.loc[i] if t)

            elif self._split_icon == "年月日":  # 判斷是否選擇年月日連接，若為年月日，另外相連
                if self._datadf.loc[i, "Day"]:  # 以 join 加 if 的判斷式，若  日  為空格 則不加入 日
                    combinelist = self._datadf.loc[i, "Year"]+"年" + \
                        self._datadf.loc[i, "Month"]+"月" + \
                        self._datadf.loc[i, "Day"]+"日"
                else:
                    combinelist = self._datadf.loc[i, "Year"] + \
                        "年"+self._datadf.loc[i, "Month"]+"月"

            self.datelist.append(combinelist)

        return self.datelist


def main():
    path = input("輸入檔案路徑:")
    colname = input("日期所在的欄位名:")
    #path2 = input("輸出檔案路徑:")
    #yearform = input("民國年")
    #split_icon = input("/")

    date_c = DATin(path, colname)  # 進入DATin 運算，創造轉型後data
    date_output_form = DATout(date_c.pickup(), ".", "民國年")

    date_output = date_c.df_origin()
    date_output[colname] = date_output_form.combine()

    print(date_output)


if __name__ == '__main__':
    main()
