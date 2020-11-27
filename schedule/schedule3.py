from tkinter import *

root = Tk()

label1 = Label(root, text="Enter Number")
E1 = Entry(root, bd=5)


def isPrime(lbl):
    entry1 = int(E1.get())
    for d in range(2, entry1):
        if entry1 % d == 0:
            lbl.config(text="Not prime")
            break
    else:
        lbl["text"] = "Prime"


submit = Button(root, text="Submit", command=lambda: isPrime(label1))

label1.pack()
E1.pack()
submit.pack(side=BOTTOM)
root.mainloop()
