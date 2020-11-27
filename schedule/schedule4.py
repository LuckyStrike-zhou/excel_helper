import tkinter as tk

root = tk.Tk()

sb = tk.Scrollbar(root)
sb.pack(side="right", fill="y")

lb = tk.Listbox(root, yscrollcommand=sb.set)

for i in range(1000):
    lb.insert("end", str(i))

lb.pack(side="left", fill="both")

sb.config(command=lb.yview)

root.mainloop()