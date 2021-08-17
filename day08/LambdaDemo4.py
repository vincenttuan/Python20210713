# 匯率
# ntd 台幣, usd 美金, jpy 日幣
exchange = {
    'usd': lambda ntd: print(ntd/30),
    'jpy': lambda ntd: print(ntd * 4)
}

ntd = 900
exchange.get('usd')(ntd)
exchange.get('jpy')(ntd)
