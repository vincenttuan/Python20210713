import json
import day07.Util as u
import requests

#file = open('桃園公共自行車即時服務資料.json', 'r', encoding='utf-8')
#data = file.read()
url = "https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"
data = requests.get(url).text
youbike = json.loads(data)

# Lab 請列出所有站台的名稱 sna
# 提示:利用 for 迴圈
# 串列變數 = range(起始值, 終止值) # 不含終止值

# 我所在地的經緯度 24.99047, 121.31187 桃園市民權路6號
my_lat = 24.99047
my_lng = 121.31187
d = 400  # (公尺)m
for no in range(2001, 2412):
    sno = str(no)
    try:
        sna = youbike['retVal'][sno]['sna']
        lat = float(youbike['retVal'][sno]['lat'])
        lng = float(youbike['retVal'][sno]['lng'])
        m, km = u.distance(my_lat, my_lng, lat, lng)
        tot = int(youbike['retVal'][sno]['tot'])
        sbi = int(youbike['retVal'][sno]['sbi'])
        bemp = int(youbike['retVal'][sno]['bemp'])
        if m <= d:
            print(sno, sna, "%dm" % int(m), "%.1fkm" % km, tot, sbi, bemp)
    except:
        pass

