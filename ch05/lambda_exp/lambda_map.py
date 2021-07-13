# map() - 값을 매핑(맞춰서 계산)

li = [1, 2, 3, 4, 5]

li2 = map(lambda x : x * 3, li)  # map(함수, 자료형)

print(list(li2))  # --> 그냥 print(li2)하면 오류,

print(list(map(lambda x : x * 3, li)))  # --> 한줄로 표현



# filter() - 어떤 조건으로 값을 필터함.

li3 = filter(lambda x : x < 4, li)  # --> 4보다 작은 요소를 추출함.
print(list(li3))

print(list(filter(lambda x : x < 4, li)))  # --> 한줄표현