# abs(x) 직접 정의해보기

# 절대값 알고리즘 1

import math

def abs_sign(x):
    if x < 0:
        return x * -1
    else:
        return x
# 절대값 2

def abs_square(x):
    y = x * x
    return math.sqrt(y) #제곱근 함수


n1 = abs_sign(-3)
n2 = abs_sign(3)
n3 = abs_square(-3)

print(n1)
print(n2)
print(n3)
