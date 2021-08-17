import json
import requests
import datetime

key = '24dff84e620603b6711c1755709c53a7'  # 請用自己的 key
q = 'taoyuan,tw'
url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (q, key)
print(url)

# description, temp, feels_like, humidity
# 1. 抓取文字資料
data = requests.get(url).text
print(data)
# 2. 將文字資料轉成 json 物件(結構化的dict), 目的: 便於日後分析
root = json.loads(data)
print(root)
# 3. 分析資料
description = root['weather'][0]['description']
temp = root['main']['temp'] - 273.15
feels_like = root['main']['feels_like'] - 273.15
humidity = root['main']['humidity']
dt = root['dt']
# 4. 列印資料
print(datetime.datetime.fromtimestamp(dt))
print("地區: %s" % q)
print("天氣概述: %s" % description)
print("溫度(℃): %.2f" % temp)
print("體感(℃): %.2f" % feels_like)
print("濕度(%%): %d" % humidity)
# 5. 取得 icon
icon = root['weather'][0]['icon']
print("icon: %s" % icon)
icon_url = 'https://openweathermap.org/img/wn/%s@4x.png' % icon
icon_data = requests.get(icon_url).content
print(icon_data)
# 6. 將 icon_data 存成 png 檔案
file = open('weather_icon.png', 'wb')
file.write(icon_data)




