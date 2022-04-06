from platform import platform
import tkinter as tk
import tkinter.messagebox
from tkinter import Variable, filedialog
from tkinter.ttk import Button
import DATE
import pandas as pd


class DAT(object):
    def __init__(self):
        # 創建窗口
        self.window = tkinter.Tk()
        # 设置窗口大小
        self.window.geometry('500x400')
        # 设置窗口标题
        self.window.title('日期統一格式系統')
        # 创建标签对象并添加到顶层窗口

        # 載入油圖
        # 創造放圖的畫布
        canvas = tk.Canvas(self.window, width=150, height=400, bg="black")
        # 圖檔位置 # 必須為全局變量 不然會消失
        #global image_file
        self.image_file = tk.PhotoImage(file="./pic.png")
        # 圖的錨定點
        #global image
        self.image = canvas.create_image(
            75, 0, anchor="n", image=self.image_file)
        canvas.pack(side="left")
        tk.Label(self.window, text='日期轉換程式', font=('標楷體', 16)).pack()
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------------

        # key 入資料位置   ## 1.輸入檔案位置 2.日期欄位 3.輸出分隔式 4.輸出年分民國OR 西元  5.輸出檔案位置
        tk.Label(self.window, text="輸入檔案位置 (須為excel or csv 檔): ",
                 font=('標楷體', 12)).place(x=160, y=30)

        tk.Label(self.window, text="日期欄位名: ",
                 font=('標楷體', 12)).place(x=160, y=100)

        tk.Label(self.window, text="日期分隔符號", font=(
            '標楷體', 12)).place(x=160, y=170)  # 下拉式

        tk.Label(self.window, text="年份格式", font=(
            '標楷體', 12)).place(x=160, y=240)  # check box

        tk.Label(self.window, text="輸出檔案位置(須為excel or csv 檔): ",
                 font=('標楷體', 12)).place(x=160, y=310)

        # 使用者登入輸入框entry
        # FOR 輸入檔案位置 日期  輸出檔案位置(須為excel檔
        # path1文字框-------------------------------------------------------------------------------------------------------------------------------------------------
        self.path1 = tk.StringVar()
        self.path1.set('C:/')
        self.entry_path1 = tk.Entry(
            self.window, textvariable=self.path1, font=('Arial', 12), width=30)
        self.entry_path1.place(x=160, y=60)
        # path1的按鈕，引用path1_button函數
        self.path1_button = tk.Button(
            self.window, text="輸入檔案", command=self.path1_button)
        self.path1_button.place(x=430, y=60)

        # 日期欄位名文字框-------------------------------------------------------------------------------------------------------------------------------------------------
        self.datecol = tk.StringVar()
        self.datecol.set('eventDate')
        self.entry_datecol = tk.Entry(
            self.window, textvariable=self.datecol, font=('標楷體', 12), width=30)
        self.entry_datecol.place(x=160, y=130)

        # 日期分割符號下拉式選單-------------------------------------------------------------------------------------------------------------------------------------------------
        self.optionList = ("無", "/", ".", "-", ",", "年月日")
        self.v = tk.StringVar()
        self.v.set("無")
        self.optionmenu = tk.OptionMenu(self.window, self.v, *self.optionList)
        self.optionmenu.place(x=160, y=200)

        # 西元年/民國年分割符號選單-------------------------------------------------------------------------------------------------------------------------------------------------
        self.yearcategorize = tk.StringVar()

        rdioOne = tk.Radiobutton(
            self.window, text='西元年', variable=self.yearcategorize, value="西元年", font=('標楷體', 12))
        rdioOne.place(x=160, y=270)
        rdioOne.select()  # 預設勾選

        rdioTwo = tk.Radiobutton(
            self.window, text='民國年', variable=self.yearcategorize, value="民國年", font=('標楷體', 12))
        rdioTwo.place(x=250, y=270)

        # 使用者登入輸入框entry
        # FOR 輸入檔案位置 日期  輸出檔案位置(須為excel檔
        # path2文字框-------------------------------------------------------------------------------------------------------------------------------------------------
        self.path2 = tk.StringVar()
        self.path2.set('C:/')
        self.entry_path2 = tk.Entry(
            self.window, textvariable=self.path2, font=('Arial', 12), width=30)
        self.entry_path2.place(x=160, y=340)
        # path2的按鈕，引用path2_button函數
        self.path2_button = tk.Button(
            self.window, text="輸出位址", command=self.path2_button)
        self.path2_button.place(x=430, y=340)

        # 開始跑日期區分------------------------------------------------------------------------------------------------------------------------------------------------

        self.start = tk.Button(
            self.window, text="開始輸出", command=self.start_button, font=('標楷體', 12), width=30)
        self.start.place(x=160, y=370)

        # 轉檔only
        self.start = tk.Button(
            self.window, text="開始轉檔", command=self.transform_button, font=('標楷體', 12), width=10)
        self.start.place(x=400, y=370)

        # 在介面內循環-------------------------------------------------------------------------------------------------------------------------------------------------
        self.window.mainloop()

    def path1_button(self):
        # 打開檔案選擇介面
        self.file_path1 = filedialog.askopenfilename(
            filetypes=[("Excel", "*.xlsx"), ("Excel", "*.xls"), ("CSV UTF8", "*.csv")])
        # 更變
        self.path1.set(self.file_path1)
        return self.file_path1

    def path2_button(self):
        # defaultextension 可以讓儲存時自動帶上副檔名
        self.file_path2 = filedialog.asksaveasfilename(filetypes=[(
            "Excel ONLY", "*.xlsx"), ("Excel ONLY", "*.xls"), ("CSV UTF8", "*.csv")], defaultextension=platform == ".xlsx" and ".csv")
        self.path2.set(self.file_path2)
        return self.file_path2

        # 日期區分函數
    def start_button(self):
        path1 = self.path1.get()
        colname = self.datecol.get()
        path2 = self.path2.get()
        yearform = self.yearcategorize.get()
        split_icon = self.v.get()

        if split_icon == "無":  # 若勾選無轉為空格
            split_icon = ""

        date_c = DATE.DATin(path1, colname)  # 進入DATin 運算，創造轉型後dataframe
        date_output_form = DATE.DATout(date_c.pickup(), split_icon, yearform)

        date_output = date_c.df_origin()  # 讀取原本的資料表
        date_output[colname] = date_output_form.combine()  # 將轉換後的日期列輸入資料表

        if path2.endswith(".csv"):
            date_output.to_csv(path2, encoding="utf8")
        elif path2.endswith(".xlsx"):
            date_output.to_excel(path2, index=False)

        result = tkinter.messagebox.showinfo(title='資訊提示！', message='完成')

    def transform_button(self):
        path1 = self.path1.get()
        path2 = self.path2.get()
        print(path1)

        if path1.endswith(".csv"):
            date_output = pd.read_csv(path1, encoding="utf8")
        elif path1.endswith(".xlsx"):
            date_output = pd.read_excel(path1, header=0, sheet_name=0)

        if path2.endswith(".csv"):
            date_output.to_csv(path2, encoding="utf8")
        elif path2.endswith(".xlsx"):
            date_output.to_excel(path2, index=False)

        result = tkinter.messagebox.showinfo(title='資訊提示！', message='完成')


app = DAT()
