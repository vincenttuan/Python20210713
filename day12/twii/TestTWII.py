# https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=20210819&selectType=ALL
import requests

def getList(date):
    #date = "20210819"
    url = "https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=%s&selectType=ALL" % (date)
    data = requests.get(url).text

    # "證券代號","證券名稱","殖利率(%)","股利年度","本益比","股價淨值比","財報年/季",
    # 將資料中有「"-"」變為「-1」
    data = data.replace('"-"', '-1')
    # 去除雙引號「"」
    data = data.replace('"', '')
    list = []
    for d in data.split('\r\n'):
        rows = d.split(",")
        if len(rows) == 8 and rows[0] != '證券代號':
            list.append(tuple(rows))
            #print(tuple(rows))

    return list

if __name__ == '__main__':
    list = getList("20210819")
    print(list)
