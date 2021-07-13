
import sys

args = sys.argv[1:]  #리스트형 자료
print(args)

sum = 0

for i in args:
    sum += int(i)  # 그냥하면 문자이므로 int를 붙여준다.

print(sum)

