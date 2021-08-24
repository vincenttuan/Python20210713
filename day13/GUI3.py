# 放入視窗元件
import time
import tkinter
import threading
from datetime import datetime

'''
+-------+
|  10   |
|加   減 |
|  ...  |
+-------+
若減到 0 則視窗離開 !
... = 現在時刻 2021/8/24 20:36:30
'''
def update_time():
    while True:
        try:
            now = datetime.today()
            dt.set(str(now).split(".")[0])
            time.sleep(1)
        except:
            break


def win_exit():
    time.sleep(0.5)
    win.quit()


def add():
    value = ans.get()
    value = value + 1
    ans.set(value)


def sub():
    value = ans.get()
    value = value - 1
    ans.set(value)
    if value == 0:
        t = threading.Thread(target=win_exit)  # 建立一個子執行緒
        t.start()  # 子執行緒運作

#-----------------------------------------------------------------
win = tkinter.Tk()
win.title("我的小視窗 3")
win.geometry("300x250")

#-----------------------------------------------------------------
dt = tkinter.StringVar()
t = threading.Thread(target=update_time)
t.start()
timelabel = tkinter.Label(win, textvariable=dt)
timelabel.pack()
#-----------------------------------------------------------------
ans = tkinter.IntVar()
ans.set(10)
label = tkinter.Label(win,
                      textvariable=ans,
                      bg='yellow',
                      font=('Arial', 50),
                      width=20,
                      height=2)
label.pack()
#-----------------------------------------------------------------
button1 = tkinter.Button(win, text="加", width=10, height=2, font=('Arial', 20),
                         command=add)
button1.pack(side=tkinter.LEFT)

button2 = tkinter.Button(win, text="減", width=10, height=2, font=('Arial', 20),
                         command=sub)
button2.pack(side=tkinter.RIGHT)

#-----------------------------------------------------------------

win.mainloop()
