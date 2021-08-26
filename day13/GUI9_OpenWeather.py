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
import requests
import json
from tkinter import font

def openweatherService(q):
    path = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (q, appid)
    ow = json.loads(requests.get(path).text)
    description = ow['weather'][0]['description']
    icon = ow['weather'][0]['icon']
    temp = ow['main']['temp'] - 273.15
    humidity = ow['main']['humidity']

    print(description, icon, temp, humidity)
    # 並請配置在 ＧＵＩ上面
    t_result_value.set('%.1f °C' % temp)
    h_result_value.set('%.1f %%' % humidity)
    desp_label_value.set(description)

def submit():
    q = entry.get()
    openweatherService(q)


if __name__ == '__main__':
    appid = "ab99f5242005a98291f643ea873b363d"

    win = tkinter.Tk()
    win.title('Open Weather')
    win.geometry('500x200')

    myfont = font.Font(family='Arial', size=24, weight='bold')

    entry = tkinter.Entry(font=myfont, justify=tkinter.CENTER)
    entry.insert(0, 'taoyuan,tw')
    submit_btn = tkinter.Button(text='Submit', font=myfont, command=submit)

    t_result_value = tkinter.StringVar()
    t_result_value.set('0.0 °C')
    t_label = tkinter.Label(text='temperature', font=myfont)
    t_result = tkinter.Label(textvariable=t_result_value, font=myfont)

    h_result_value = tkinter.StringVar()
    h_result_value.set('0.0 %')
    h_label = tkinter.Label(text='humidity', font=myfont)
    h_result = tkinter.Label(textvariable=h_result_value, font=myfont)

    desp_label_value = tkinter.StringVar()
    desp_label = tkinter.Label(textvariable=desp_label_value, font=myfont)
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
