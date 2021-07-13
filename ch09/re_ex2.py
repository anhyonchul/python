# {m, n} 을 사용한 반복 - m은 최소 반복횟수 n은 최대 반복 횟수

import re

str = '123?45yy7890 hi 999 Hello'

m1 = re.findall("\d{1,3}", str)
print(m1)
# \d는 숫자를 찾는것이므로 숫자를 1~3번 반복만 찾는다.
# ['123', '45', '789', '0', '999']

m2 = re.findall("[A-z]+", str)
print(m2)
# 대소문자 반복을 전부 찾는다.
# ['yy', 'hi', 'Hello']

m3 = re.findall("[1-5]{1,2}", str)
print(m3)
# 숫자 1~5사이수가 1에서 2번반복을 찾는다.
# ['12', '3', '45']