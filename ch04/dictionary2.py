# 딕셔너리 연습

person = {}

print(person)  # ---> 빈리스트가 나온다.

person['name'] = '이순신'  # ---> [key] 'value' 추가
person['age'] = 40

print(person)

person['address'] = "인천시 부평구"

print(person)

#딕셔너리의 벨류값을 출력
for value in person:
    print(person[value])

del person['address']  # dic.pop('address')와 같다.
print(person)
