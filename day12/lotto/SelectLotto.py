# 在 10000 期中, 每一個數字所出現的次數為何?
import sqlite3

conn = sqlite3.connect('lotto.db')
cursor = conn.cursor()

list = []
for i in range(49):
    n = i+1
    sql = "select count(*) as count from lotto " \
          "where n1=%d or n2=%d or n3=%d or n4=%d or n5=%d or n6=%d" % (n, n, n, n, n, n)
    cursor.execute(sql)
    count = cursor.fetchone()

    list.append({'n': n, 'num': count[0]})
    #print(n, count[0])

conn.close()

print(list)
# 請問哪一個號碼出現次數最多 ?
# 以及哪一個號碼出現次數最少 ?
seq = [x['num'] for x in list]
print(seq)
min = min(seq)
max = max(seq)
print(min, max)

for x in list:
    if x['num'] == max:
        print('max:', x)
    if x['num'] == min:
        print('min:', x)

