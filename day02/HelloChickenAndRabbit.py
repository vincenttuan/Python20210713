'''
1. 使用者輸入雞+兔的總數 (Ex: 83)
2. 使用者輸入雞的腳+兔的腳總數 (Ex: 240)
則系統會自動算出雞與兔各有幾隻 (Ex: 雞 46 兔 37)
'''

if __name__ == '__main__':
    sum = int(input('請輸入雞+兔的總數: '))
    # 奇數, 負數, 不是數字的資料(try-catch處理) ... 都會造成 sum 輸入錯誤 ...
    # 檢查 sum 是否是奇數或負數
    # homework ...

    min, max = sum * 2, sum * 4
    feet = int(input('請輸入雞的腳+兔的腳總數( %d ~ %d ): ' % (min, max)))

    # 檢查 feet 是否在 min 與 max 之間
    if(min <= feet <= max):
        rabbit = (feet - sum * 2)/2
        chicken = sum - rabbit
        print("雞:%d 兔:%d" % (chicken, rabbit))
    else:
        print('腳+兔的腳總數不在合法範圍內')
