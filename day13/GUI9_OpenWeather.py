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
import urllib
import threading
from PIL import Image, ImageTk
from io import BytesIO

from tkinter import font

def showIcon(icon):
    path = 'https://openweathermap.org/img/wn/%s@4x.png' % icon
    # 1. 圖片原始資料
    raw_data = urllib.request.urlopen(path).read()
    print(raw_data)
    # 2. 將圖片原始資料轉成 Image 物件
    img = Image.open(BytesIO(raw_data))
    # 3. 將 Image 物件轉成 Photo 物件（給 Label 使用）
    photo = ImageTk.PhotoImage(img)
    # 4. 重新配置
    icon_label = tkinter.Label(image=photo)
    icon_label.image = photo
    icon_label.grid(row=4, column=0, columnspan=2, sticky='EWNS')

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

    # 加入執行緒 2
    t2 = threading.Thread(target=showIcon, args=(icon,))
    t2.start()

def submit():
    q = entry.get()
    # 加入執行緒 1
    t1 = threading.Thread(target=openweatherService, args=(q,))
    t1.start()


if __name__ == '__main__':
    appid = "ab99f5242005a98291f643ea873b363d"

    win = tkinter.Tk()
    win.title('Open Weather')
    win.geometry('500x500')

    myfont = font.Font(family='Arial', size=24, weight='bold')

    entry = tkinter.Entry(font=myfont, justify=tkinter.CENTER)
    entry.insert(0, 'taoyuan,tw')
    submit_btn = tkinter.Button(text='查詢', font=myfont, command=submit)

    t_result_value = tkinter.StringVar()
    t_result_value.set('0.0 °C')
    t_label = tkinter.Label(text='溫度', font=myfont)
    t_result = tkinter.Label(textvariable=t_result_value, font=myfont)

    h_result_value = tkinter.StringVar()
    h_result_value.set('0.0 %')
    h_label = tkinter.Label(text='濕度', font=myfont)
    h_result = tkinter.Label(textvariable=h_result_value, font=myfont)

    desp_label_value = tkinter.StringVar()
    desp_label = tkinter.Label(textvariable=desp_label_value, font=myfont)
    icon_label = tkinter.Label(text='photo', font=myfont)

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
