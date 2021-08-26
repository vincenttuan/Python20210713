# OpenWeather
# ab99f5242005a98291f643ea873b363d
'''
OpenWeather
+------------+--------+
| taoyuan,tw | Submit |  <-- Entry, Button
+------------+--------+
|temperature |  29.1C |  <-- Label, Label
+------------+--------+
|  humidity  |   91%  |  <-- Label, Label
+------------+--------+
|      few clouds     |  <-- Label
+---------------------+
|        icon         |  <-- Label(含有 icon)
+---------------------+
'''

import tkinter
from tkinter import font

win = tkinter.Tk()
win.title('Open Weather')
win.geometry('500x200')

myfont = font.Font(family='Arial', size=24, weight='bold')

entry = tkinter.Entry(font=myfont, justify=tkinter.CENTER)
submit_btn = tkinter.Button(text='Submit', font=myfont)

t_label = tkinter.Label(text='temperature', font=myfont)
t_result = tkinter.Label(text='0.0 °C', font=myfont)

h_label = tkinter.Label(text='humidity', font=myfont)
h_result = tkinter.Label(text='0.0 %', font=myfont)

desp_label = tkinter.Label(text='?', font=myfont)
icon_label = tkinter.Label(text='?', font=myfont)

win.rowconfigure((0, 1), weight=1)  # 列 0, 1 同步放大與縮小
win.columnconfigure((0, 1), weight=1)  # 欄 0, 1 同步放大與縮小

entry.grid(row=0, column=0, columnspan=1, sticky='EWNS')
submit_btn.grid(row=0, column=1, columnspan=1, sticky='EWNS')
t_label.grid(row=1, column=0, columnspan=1, sticky='EWNS')
t_result.grid(row=1, column=1, columnspan=1, sticky='EWNS')
h_label.grid(row=2, column=0, columnspan=1, sticky='EWNS')
h_result.grid(row=2, column=1, columnspan=1, sticky='EWNS')
desp_label.grid(row=3, column=0, columnspan=2, sticky='EWNS')
icon_label.grid(row=4, column=0, columnspan=2, sticky='EWNS')

win.mainloop()
