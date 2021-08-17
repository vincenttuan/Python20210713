word = '台積電每股買價:599;賣價:601;成交價:600'
array = word.split(";")
print(array)
bid = array[0].split(":")[1]
ask = array[1].split(":")[1]
price = array[2].split(":")[1]

bid = float(bid)      # String 轉 float
ask = float(ask)      # String 轉 float
price = float(price)  # String 轉 float

print(bid, ask, price)

# 1. 若要買進2000股，需要多少錢 (看成交價) ?
print(2000 * price)

# 2. 若要市價買進1000股，需要多少錢 (看賣價) ?
print(2000 * ask)

# 3. 若要市價賣出1000股，需要多少錢 (看買價) ?
print(2000 * bid)