def check_score(score):
    if score >= 60:
        return "Pass"
    else:
        return "Fail"

if __name__ == '__main__':
    score = 80
    result = check_score(score)
    # result 就僅僅只是一個結果
    print(score, result)
    #-----------------------------------------------
    score = 80
    result = "Pass" if score >= 60 else "Fail"
    # result 就僅僅只是一個結果
    print(score, result)
    # -----------------------------------------------
    result = lambda score: "Pass" if score >= 60 else "Fail"
    # result 就是一個 lambda 的運算式
    print(result)
    print(70, result(70))
    print(80, result(80))
    print(40, result(40))
    # -----------------------------------------------
    temp = lambda : print("現在溫度 26.6 度")
    temp()