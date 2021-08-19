import sqlite3
import random

conn = sqlite3.connect('lotto.db')
cursor = conn.cursor()

lottos = []

for i in range(10000):
    # 取出 1~49 不重複的數字
    nums = set()
    while len(nums) < 6:
        nums.add(random.randint(1, 49))

    # 加入到 lottos
    # 注意若要將數組加入到資料庫中必須轉成元祖(tuple)
    lottos.append(tuple(nums))

print(len(lottos), lottos)

sql = 'Insert into lotto(n1, n2, n3, n4, n5, n6) values (?,?,?,?,?,?)'
cursor.executemany(sql, lottos)
conn.commit()
conn.close()

print('批次新增成功')