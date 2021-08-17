# 經由網路擷取 json 字串並加以分析
import json
import requests

path = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'
data = requests.get(path).text  # 取得網址內容的原始字串資料
rices = json.loads(data)
print(len(rices))

num = 0
for rice in rices:
    if rice['品名'].find('台稉') != -1:
        num = num + 1
        print(num, rice['品名'], rice['不合格原因'])

