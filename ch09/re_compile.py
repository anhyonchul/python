# 정규 표현식 예제

import re

p = re.compile('[a-z]+')  # +는 반복을 의미하는 메타 문자
m = p.match('afternoon')
print(m)

p = re.compile('ca+t')  # +는 앞문자 1개 이상의 메타 문자
a = p.match('caaaaat')
print(a)

p = re.compile('a.b') # .은 숫자를 포함한 임의의 문자 1개 메타 문자
m1 = p.match('avb')
print(m1)