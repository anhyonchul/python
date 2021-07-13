import re

str = "ahn 010-1234-5678"
pat = re.compile("(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)")

#pat = re.compile("(\w+)\s+(\d+[-]\d+[-]\d+)")     # 이거의 경우 sub를 사용 하려면
#m = re.search(pat, str)
#print(m.group(0)) # 전체 문자열
#print(m.group(1)) # 1번 그룹()
#print(m.group(2)) # 2번 그룹()

# sub 매서드 사용

s = pat.sub("\g<name> \g<phone>", str)
#s = pat.sub("\g<1> \g<2>", str)                    # 이렇게 하면 된다.
print(s)