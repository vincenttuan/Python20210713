from math import radians, cos, sin, asin, sqrt

# 計算地球經緯度二點間的距離
def distance(lat1, lng1, lat2, lng2):
    # 將十進制的度數轉換為弧度
    lat1, lng1, lat2, lng2 = map(radians, [lat1, lng1, lat2, lng2])
    # 半正矢公式
    dlng = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlng/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球半徑
    km = c * r
    m = km * 1000
    return m, km