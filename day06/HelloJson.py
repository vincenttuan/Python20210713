import json

x = '{"name":"John", "age":18}'
person = json.loads(x)
print(type(person))
print(person['name'], person['age'])

x = '{"name":"John", "age":18, "profile":{"w":60.0, "h":170.0}}'
# 計算出 John 的 bmi = ?
person = json.loads(x)
profile = person["profile"]
print(type(profile), profile)
w = profile['w']
h = profile['h']
print(type(w), w, type(h), h)
bmi = w / (h/100)**2
print(bmi)

x = '[{"name":"John", "age":18, "profile":{"w":60.0, "h":170.0}},' \
    '{"name":"Mary", "age":17, "profile":{"w":55.0, "h":162.5}}]'
# 計算出 John, Mary 的 bmi(小數點第二位) = ?
people = json.loads(x)
print(type(people))
for person in people:
    name = person['name']
    w = person['profile']['w']
    h = person['profile']['h']
    #print(type(w), type(h))
    bmi = w / pow(h/100, 2)
    print("%s bmi= %.2f" % (name, bmi))
