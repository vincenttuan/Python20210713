'''
BMI 計算機
+--------+---------+
| Height |  170.0  |  <-- Label, Entry
+--------+---------+
| Weight |   60.5  |  <-- Label, Entry
+--------+---------+
|  Reset |  Submit |  <-- Button, Button
+--------+---------+
|   BMI  |  20.76  |  <-- Label, Label
+--------+---------+

'''
import tkinter
from tkinter import font

def calc():
    h = float(h_entry.get())
    w = float(w_entry.get())
    bmi = w / (h/100)**2
    result.set("%.2f" % bmi)

def clean():
    # 清除欄位資料
    h_entry.delete(0, tkinter.END)
    w_entry.delete(0, tkinter.END)
    # 還原成預設值
    h_entry.insert(0, '0')
    w_entry.insert(0, '0')
    result.set("0.00")

win = tkinter.Tk()
win.title("BMI 計算機")
win.geometry("600x250")
myfont = font.Font(family='Arial', size=36, weight='bold')

h_label = tkinter.Label(text='Height', font=myfont)
h_entry = tkinter.Entry(font=myfont, justify=tkinter.CENTER)
h_entry.insert(0, '0')

w_label = tkinter.Label(text='Weight', font=myfont)
w_entry = tkinter.Entry(font=myfont, justify=tkinter.CENTER)
w_entry.insert(0, '0')

reset_btn = tkinter.Button(text='Reset', font=myfont, command=clean)
submit_btn = tkinter.Button(text='Submit', font=myfont, command=calc)

bmi_label = tkinter.Label(text='BMI', font=myfont)
result = tkinter.StringVar()
result.set("0.00")
result_label = tkinter.Label(textvariable=result, font=myfont)

win.rowconfigure((0, 1), weight=1)  # 列 0, 1 同步放大與縮小
win.columnconfigure((0, 1), weight=1)  # 欄 0, 1 同步放大與縮小

h_label.grid(row=0, column=0, columnspan=1, sticky='EWNS')
h_entry.grid(row=0, column=1, columnspan=1, sticky='EWNS')
w_label.grid(row=1, column=0, columnspan=1, sticky='EWNS')
w_entry.grid(row=1, column=1, columnspan=1, sticky='EWNS')
reset_btn.grid(row=2, column=0, columnspan=1, sticky='EWNS')
submit_btn.grid(row=2, column=1, columnspan=1, sticky='EWNS')
bmi_label.grid(row=3, column=0, columnspan=1, sticky='EWNS')
result_label.grid(row=3, column=1, columnspan=1, sticky='EWNS')

win.mainloop()





