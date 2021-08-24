# 放入視窗元件
import tkinter
from tkinter import messagebox
'''
+-------+
| Label |
|B1   B2|
+-------+
'''

def show_message():
    messagebox.showinfo('Hello', 'Message...')

def win_exit():
    win.quit()

win = tkinter.Tk()

win.title('我的小視窗 2')
win.geometry("300x200")

label = tkinter.Label(win,
                      text='Hello',
                      bg='yellow',
                      font=('Arial', 20),
                      width=30,
                      height=5)
label.pack()

button1 = tkinter.Button(win, text="OK", width=10, height=2, font=('Arial', 20),
                         command=show_message)
button1.pack(side=tkinter.LEFT)

button2 = tkinter.Button(win, text="Exit", width=10, height=2, font=('Arial', 20),
                         command=win_exit)
button2.pack(side=tkinter.RIGHT)

win.mainloop()


