import sqlite3

from day12.twii.TestTWII import getList

def insert(date):
    list = getList(date)
    conn = sqlite3.connect('twii.db')
    cursor = conn.cursor()
    print(list)

    for data in list:
        report_date = int(date)
        stock_code = data[0]
        securities_name = data[1]
        yield_rate = float(data[2])
        div_year = int(data[3])
        pe = float(data[4])
        pb = float(data[5])
        fin_report = data[6]
        memo = data[7]
        sql = "Insert into twii(report_date, stock_code, securities_name, yield_rate, div_year, pe, pb, fin_report, memo) " \
              "values (%d, '%s', '%s', %f, %d, %f, %f, '%s', '%s')" % (report_date, stock_code, securities_name, yield_rate, div_year, pe, pb, fin_report, memo)
        cursor.execute(sql)

    conn.commit()
    conn.close()
    print('Insert OK')

if __name__ == '__main__':
    insert('20210819')