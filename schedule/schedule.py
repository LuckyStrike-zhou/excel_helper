from tkinter import *
import time


# 更新进度条函数
def change_schedule(now_schedule, all_schedule):
    canvas.coords(fill_rec, (5, 5, 6 + (now_schedule / all_schedule) * 100, 25))
    root.update()
    x.set(str(round(now_schedule / all_schedule * 100, 2)) + '%')
    if round(now_schedule / all_schedule * 100, 2) == 100.00:
        x.set("完成")


root = Tk()
# 创建画布
frame = Frame(root).grid(row=0, column=0)  # 使用时将框架根据情况选择新的位置
canvas = Canvas(frame, width=120, height=30, bg="white")
canvas.grid(row=0, column=0)
x = StringVar()
# 进度条以及完成程度
out_rec = canvas.create_rectangle(5, 5, 105, 25, outline="blue", width=1)
fill_rec = canvas.create_rectangle(5, 5, 5, 25, outline="", width=0, fill="blue")

Label(frame, textvariable=x).grid(row=0, column=1)

'''
使用时直接调用函数change_schedule(now_schedule,all_schedule)
下面就模拟一下....
'''

for i in range(100):
    time.sleep(0.1)
    change_schedule(i, 99)

mainloop()
