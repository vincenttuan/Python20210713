# lambda lab:
# 請利用 lambda 做出能夠判斷 odd 奇數, even 偶數的函式
# result(4) 得到 "even"
# result(3) 得到 "odd"
# 印出結果的函式也一律使用 lambda
# 假設 n = 3 印出 odd
#     n = 4 印出 even

result      = lambda n : "Even" if n % 2 == 0 else "Odd"
printResult = lambda n, x : print(n, x)

n = 3
printResult(n, result(n))
n = 4
printResult(n, result(n))
