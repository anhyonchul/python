import re

# ()로 구분해서 이름과 전화번호를 분리해서 추출
p = re.compile("(\w+)\s(\d+[-]\d+[-]\d+)")  #\s는 공백
s = p.search("jang 010-1234-5678")
print(s.group(1))  # group은 문자열을 표시해주는 함수
print(s.group(2))


# re_grouping

p2 = re.compile("blue|red")
s2 = p2.sub('color', 'blue socks and red shoes')  # blue, red를 color로 변경
print(s2)