import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilenames()
for f in file_path:
    fo = f.split('.')[0]+'.csv'
    with open(fo, 'w') as foo:
        with open(f, 'r') as fn:
            fn.readline()
            for line in fn.readlines():
                li = line.strip().split()
                foo.write('%f,%f\n' % (float(li[1]), float(li[0])))
                print(li)
