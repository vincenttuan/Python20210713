import random
import tkinter
from tkinter import font
import threading
import time
'''
+---+---+---+---+
| 2 | 3 | 1 | 7 |
+---+---+---+---+
|  Play |  Exit |
+-------+-------+
'''
def generateValue(count, value):
    for i in range(count):
        n = random.randint(0, 9)
        value.set(n)
        time.sleep(0.05)

def play():
    list = [(30, value1), (60, value2), (90, value3), (120, value4)]
    for item in list:
        t = threading.Thread(target=generateValue, args=(item[0], item[1],))
        t.start()


win = tkinter.Tk()
win.title("我的小視窗 4")
win.geometry("500x250")

value1 = tkinter.IntVar()
value2 = tkinter.IntVar()
value3 = tkinter.IntVar()
value4 = tkinter.IntVar()

myfont = font.Font(family='Arial', size=36, weight='bold')
n1 = tkinter.Button(textvariable=value1, font=myfont)
n2 = tkinter.Button(textvariable=value2, font=myfont)
n3 = tkinter.Button(textvariable=value3, font=myfont)
n4 = tkinter.Button(textvariable=value4, font=myfont)
b1 = tkinter.Button(text='Play', font=myfont, command=play)
b2 = tkinter.Button(text='Exit', font=myfont)

win.rowconfigure((0, 1), weight=1) # 列 0, 1 同步放大與縮小
win.columnconfigure((0, 1, 2, 3), weight=1) # 欄 0, 1, 2, 3 同步放大與縮小

n1.grid(row=0, column=0, columnspan=1, sticky='EWNS') # EWNS 無縫填滿
n2.grid(row=0, column=1, columnspan=1, sticky='EWNS') # EWNS 無縫填滿
n3.grid(row=0, column=2, columnspan=1, sticky='EWNS') # EWNS 無縫填滿
n4.grid(row=0, column=3, columnspan=1, sticky='EWNS') # EWNS 無縫填滿
b1.grid(row=1, column=0, columnspan=2, sticky='EWNS') # EWNS 無縫填滿
b2.grid(row=1, column=2, columnspan=2, sticky='EWNS') # EWNS 無縫填滿

win.mainloop()
