id = 'A123456789'
sex = id[1]  # 1: 男生, 2: 女生

printSex = {  # dict 結構
    "1": lambda: print("男生"),
    "2": lambda: print("女生")
}

printSex.get(sex)()  # 最後要加上(), 因為是函式

sexObj = printSex.get(sex)
sexObj()
