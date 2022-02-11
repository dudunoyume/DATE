import tkinter as tk
import tkinter.messagebox
from tkinter import Variable, filedialog
from tkinter.ttk import Button
import DATE


class DAT():

    def __init__(self):
        # 創建窗口
        self.window = tkinter.Tk()
        # 设置窗口大小
        self.window.geometry('500x300')
        # 设置窗口标题
        self.window.title('日期統一格式系統')
        # 创建标签对象并添加到顶层窗口

        # 載入油圖
        # 創造放圖的畫布
        canvas = tk.Canvas(self.window, width=150, height=300, bg="black")
        # 圖檔位置 # 必須為全局變量
        #global image_file
        self.image_file = tk.PhotoImage(file='shishiro.png')
        # 圖的錨定點
        #global image
        self.image = canvas.create_image(
            75, 0, anchor="n", image=self.image_file)
        canvas.pack(side="left")
        tk.Label(self.window, text='獅白牡丹歡迎你', font=('標楷體', 16)).pack()

        # key 入資料位置   ## 1.輸入檔案位置 2.日期欄位 3.輸出檔案位置 4.輸出分隔式 5.輸出年分民國OR 西元
        tk.Label(self.window, text="輸入檔案位置 (須為excel檔): ",
                 font=('標楷體', 12)).place(x=160, y=30)

        tk.Label(self.window, text="日期欄位名: ",
                 font=('標楷體', 12)).place(x=160, y=80)

        tk.Label(self.window, text="日期分隔符號", font=(
            '標楷體', 12)).place(x=160, y=130)  # 下拉式

        tk.Label(self.window, text="年份格式", font=(
            '標楷體', 12)).place(x=160, y=180)  # check box

        tk.Label(self.window, text="輸出檔案位置(須為excel檔): ",
                 font=('標楷體', 12)).place(x=160, y=230)

        # 使用者登入輸入框entry
        # FOR 輸入檔案位置 日期  輸出檔案位置(須為excel檔
        self.path1 = tk.StringVar()
        self.path1.set('C:/')
        self.entry_path1 = tk.Entry(
            self.window, textvariable=self.path1, font=('Arial', 12), width=30)
        self.entry_path1.place(x=160, y=50)
        # path1的按鈕
        self.path1_button = tk.Button(
            self.window, text="輸入檔案", command=self.path1_button)
        self.path1_button.place(x=430, y=50)

        self.path2 = tk.StringVar()
        self.path2.set('C:/')
        self.entry_path2 = tk.Entry(
            self.window, textvariable=self.path2, font=('Arial', 12), width=30)
        self.entry_path2.place(x=160, y=250)
        # path1的按鈕
        self.path2_button = tk.Button(
            self.window, text="輸出檔案", command=self.path2_button)
        self.path2_button.place(x=430, y=250)

        self.window.mainloop()

    def path1_button(self):
        self.file_path1 = filedialog.askopenfilename(
            filetypes=[("Excel ONLY", "*.xlsx"), ("Excel ONLY", "*.xls")])
        self.path1.set(self.file_path1)
        return self.file_path1

    def path2_button(self):
        self.file_path2 = filedialog.askopenfilename(
            filetypes=[("Excel ONLY", "*.xlsx"), ("Excel ONLY", "*.xls")])
        self.path2.set(self.file_path2)
        return self.file_path2


app = DAT()
