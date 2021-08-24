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
    pass

def sub():
    pass

win = tkinter.Tk()
win.title("我的小視窗 3")
win.geometry("300x200")

label = tkinter.Label(win,
                      text='10',
                      bg='yellow',
                      font=('Arial', 20),
                      width=30,
                      height=5)
label.pack()

button1 = tkinter.Button(win, text="加", width=10, height=2, font=('Arial', 20),
                         command=add)
button1.pack(side=tkinter.LEFT)

button2 = tkinter.Button(win, text="減", width=10, height=2, font=('Arial', 20),
                         command=sub)
button2.pack(side=tkinter.RIGHT)

win.mainloop()