from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import os
import pandas as pd
import xlrd
import xlwt
import time

concat_excels_name = '合并表格.xlsx'
summary_name = '汇总表格.xlsx'


# 将目录文件夹下所有xlsx文件合并
def concat_excels():
    if not os.path.exists(dir_path.get()):
        messagebox.showerror(title="合并错误", message="目录错误")
        return
    excels = [
        pd.read_excel(os.path.join(dir_path.get(), fname))
        for fname in os.listdir(dir_path.get())
        if '.xlsx' in fname
    ]
    df = pd.concat(excels)
    df.to_excel(os.path.join(dir_path.get(), concat_excels_name), index=False)
    messagebox.showinfo(title="合并完成！", message="请查看：" + concat_excels_name)


# 将目录文件夹下所有xlsx文件
def count_excels():
    messagebox.showinfo(title="提示", message="暂未实现")


# 选择目录
def select_path():
    dir_path.set(askdirectory())


def radio_print():
    print(radio_int.get())


# 日期转换
def vaild_date(str):
    try:
        time.strftime(str, "%Y-%m-%d")
        return True
    except:
        return False


# 汇总表格
def summary_excels_data():
    if not os.path.exists(dir_path.get()):
        messagebox.showerror(title="合并错误", message="目录错误")
        return
    keywords = summary.get()
    kw_arr = keywords.split('-')
    if len(kw_arr) < 2 and ('' in kw_arr):
        messagebox.showerror(title="合并错误", message="没有关键词")
        return
    rd_excels = [
        xlrd.open_workbook(os.path.join(dir_path.get(), fname))
        for fname in os.listdir(dir_path.get())
        if '.xlsx' in fname
    ]
    data_arr = []
    for book in rd_excels:
        sheet1 = book.sheet_by_index(0)
        index_arr = []
        for i in range(sheet1.ncols):
            cell_value = sheet1.cell_value(0, i)
            if cell_value in kw_arr:
                index_arr.append(i)
        for j in range(sheet1.nrows):
            row_data = []
            for k in index_arr:
                dv = sheet1.cell_value(j, k)
                row_data.append(dv)
            # print('行数据：', row_data)
            if len(row_data) > 0:
                data_arr.append(row_data)
    if len(data_arr) == 0:
        messagebox.showerror(title="合并错误", message="关键词错误")  # 容错处理
        return
    r_book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    r_sheet = r_book.add_sheet("sheet1", cell_overwrite_ok=True)
    # print(data_arr)
    for r_i in range(len(data_arr)):
        for r_j in range(len(data_arr[i])):
            r_sheet.write(r_i, r_j, data_arr[r_i][r_j])
    r_book.save(os.path.join(dir_path.get(), summary_name))
    messagebox.showinfo(title="汇总完成！", message="请查看：" + summary_name)


root = Tk()
root.title("安海燕大宝贝专用表格工具~❤")

dir_path = StringVar()  # 全局目录地址
radio_int = IntVar()  # 首行标题
summary = StringVar()  # 汇总

# 目录选择
Label(root, text="目标路径:").grid(row=0, column=0)
Entry(root, textvariable=dir_path).grid(row=0, column=1)
Button(root, text="路径选择", command=select_path, highlightbackground='gray').grid(row=0, column=2)
# 自动合并
auto_merge = Button(root, text="开始合并", command=concat_excels, highlightbackground='gray').grid(row=1, column=0)
Label(root, text="（选择目录后点击按钮）").grid(row=1, column=1)

# 首行标题选项
# Label(root, text="首行标题:").grid(row=2, column=0)
# radio_int.set(1)
# r1 = Radiobutton(root, text="有", command=radio_print, value=1, variable=radio_int,  bg='blue').grid(row=2, column=1)
# r2 = Radiobutton(root, text="无", command=radio_print, value=0, variable=radio_int,  bg='blue').grid(row=2, column=2)
# 自动计数
# auto_count = Button(root, text="自动统计", command=count_excels, highlightbackground='gray').grid(row=3, column=0)
# Label(root, text="（选择目录和首行标题后点击按钮）").grid(row=3, column=1)

# 自动汇总
Label(root, text="汇总关键词(以-分隔)：").grid(row=5, column=0)
Entry(root, textvariable=summary).grid(row=5, column=1)
auto_summary = Button(root, text="自动汇总", command=summary_excels_data, highlightbackground='gray').grid(row=6, column=0)

root.mainloop()
