# 簡易選股
# yield_rate > 7 把股票當作定存
# pe 本益比 < 10
# pb > 1 高估(適合賣出) pb < 1 低估(適合買進)
import sqlite3

if __name__ == '__main__':

    conn = sqlite3.connect('twii.db')
    cursor = conn.cursor()

    sql = 'select report_date, stock_code, securities_name, yield_rate, pe, pb ' \
          'from twii ' \
          'where yield_rate > 7 and pe < 10 and pb < 1'

    cursor.execute(sql)

    for row in cursor.fetchall():
        print('{}\t{}\t{}\t{}\t{}\t{}'
              .format(row[0], row[1], row[2], row[3], row[4], row[5]))

