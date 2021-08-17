
if __name__ == '__main__':
    print("計算 BMI")
    h = 170  # 身高
    w = 60   # 體重
    bmi = w / ((h/100)*(h/100))
    print(h, w, bmi)
    bmi = w / (h/100)**2
    print(h, w, bmi)
    print("身高:", h, "體重:", w, "BMI:", bmi)
    # %d 整數  %f 浮點數  %s 字串  %b 布林值
    print("身高:%f 體重:%f BMI:%f" % (h, w, bmi))
    print("身高:%.1f 體重:%.1f BMI:%.2f" % (h, w, bmi))
