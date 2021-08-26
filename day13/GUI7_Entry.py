import tkinter
from tkinter import messagebox as msg

def get():
    value = entry.get()
    msg.showinfo('取得資料', '%s %s' % (value, type(value)))

win = tkinter.Tk()
win.title('輸入框')
win.geometry("300x200")
entry = tkinter.Entry(win, justify=tkinter.CENTER, font=('Arial', 50))
entry.insert(0, '?')
entry.pack()

b1 = tkinter.Button(win, text="Get", font=('Arial', 50), command=get)
b1.pack()

win.mainloop()
