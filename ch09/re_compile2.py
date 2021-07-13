# 정규 표현식 예제

import re
            # '[0-9A-Za-z]' = '\w' 전체 문자
p = re.compile('[a-z]+')  # +는 반복을 의미하는 메타 문자

m = p.match('2021 incheon')  # --> 처음에는 일치(match)하는 문자가 없다. 비슷한게 find()
print(m)

s = p.search("2021 incheon")  # --> 전체로 검색(search)해서 문자를 찾았다.
print(s)

p2 = re.compile('\w+\s\w+')   # --> \s는 한칸 띄우기 '전체 + 한칸 + 전체'
m2 = p2.match("2021 incheon")
print(m2)