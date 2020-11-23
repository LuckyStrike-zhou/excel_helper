from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import messagebox

def selectPath():
    path_ = askdirectory()
    path.set(path_)


def radio_print():
    print(r_string.get())

def data_merge():
    messagebox.showinfo(title="提示", message="data_merge")


root = Tk()
root.title("表格工具")
path = StringVar()  # 路径
r_string = IntVar()  # 首行标题
summary = StringVar()  # 汇总

# 目录选择
Label(root, text="目标路径:").grid(row=0, column=0)
Entry(root, textvariable=path).grid(row=0, column=1)
Button(root, text="路径选择", command=selectPath, highlightbackground='gray').grid(row=0, column=2)
# 自动合并
auto_merge = Button(root, text="开始合并", highlightbackground='gray').grid(row=1, column=0)
Label(root, text="（选择目录后点击按钮）").grid(row=1, column=1)

# 首行标题选项
Label(root, text="首行标题:").grid(row=2, column=0)
r_string.set(1)
r1 = Radiobutton(root, text="有", command=radio_print, value=1, variable=r_string,  bg='blue').grid(row=2, column=1)
r2 = Radiobutton(root, text="无", command=radio_print, value=2, variable=r_string,  bg='blue').grid(row=2, column=2)
# 自动计数
auto_count = Button(root, text="自动统计", command=data_merge, highlightbackground='gray').grid(row=3, column=0)
Label(root, text="（选择目录和首行标题后点击按钮）").grid(row=3, column=1)

# 自动汇总
Label(root, text="汇总关键词(以-分隔)：").grid(row=5, column=0)
Entry(root, textvariable=summary).grid(row=5, column=1)
auto_summary = Button(root, text="自动汇总", command=data_merge, highlightbackground='gray').grid(row=6, column=0)


root.mainloop()