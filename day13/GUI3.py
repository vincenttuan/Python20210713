# 放入視窗元件
import tkinter

'''
+-------+
|  10   |
|加   減 |
+-------+
若減到 0 則視窗離開 !
'''


def add():
    value = ans.get()
    value = value + 1
    ans.set(value)


def sub():
    value = ans.get()
    value = value - 1
    ans.set(value)


win = tkinter.Tk()
win.title("我的小視窗 3")
win.geometry("300x200")

ans = tkinter.IntVar()
ans.set(10)
label = tkinter.Label(win,
                      textvariable=ans,
                      bg='yellow',
                      font=('Arial', 50),
                      width=20,
                      height=2)
label.pack()

button1 = tkinter.Button(win, text="加", width=10, height=2, font=('Arial', 20),
                         command=add)
button1.pack(side=tkinter.LEFT)

button2 = tkinter.Button(win, text="減", width=10, height=2, font=('Arial', 20),
                         command=sub)
button2.pack(side=tkinter.RIGHT)

win.mainloop()
