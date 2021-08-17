import re
# split 與 dict
exam = "國文=100,數學=90,英文=80"
exam_dict = dict(ex.split("=") for ex  in exam.split(","))

print(1, exam_dict)
print(2, exam_dict['國文'])
print(3, exam_dict.values())
print(4, list(exam_dict.values()))
print(5, list(map(int, exam_dict.values())))
print(6, sum(list(map(int, exam_dict.values()))))

# map
s = "1 3 5 7"
s_list = s.split()
s_int_list = list(map(int, s_list))
print(s)
print(s_list)
print(s_int_list)

# 多符號切割
# split() 只允許單一符號切割
# re.split() 支援多符號切割
word = 'Hello!你今天好嗎？再會。20210729'
#['Hello', '你今天好嗎', '再會', '20210729']
word_list = re.split('!|？|。', word)
print(word_list)

