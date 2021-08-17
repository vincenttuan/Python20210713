# 利用 lambda 設計一個 bmi 函數式宣告
# bmi <= 18 "過輕", bmi > 24 "過重", 其他 "正常"
# Ex: checkBMI(bmi) 輸出 20.76 (正常)

def getBMIResult(bmi):
    if bmi <= 18:
        return "過輕"
    elif bmi > 24:
        return "過重"
    else:
        return "正常"

h = 170
w = 60

bmi_value = lambda h, w : w / (h/100)**2
check_bmi = lambda bmi : getBMIResult(bmi)

bmi = bmi_value(h, w)
print("%.2f" % bmi, check_bmi(bmi))

