'''
# 1번
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
        return self.value

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
        return self.value

# 부모 클래스의 인스턴스
c = Calculator()
print(c.add(10))
print(c.value)

cal = UpgradeCalculator()
print(cal.add(10))
print(cal.minus(7))
print(cal.value)

cal2 = MaxLimitCalculator()
print(cal2.add(50))
print(cal2.add(60))
print(cal2.value)


#4번


def positive(a):
    a2=[]
    for i in a:
        if i >= 0:
            a2.append(i)
    return a2

li = [1, -2, 3, -5, 8, -3]

li2 = positive(li)
print(li2)
#lambda - filter()를 쓰는 방식
print(list(filter(lambda x : x >= 0, li)))

#5번

# int('0xea', 16)

#6번

def times(a):
    a2 = []
    for i in a:
        a2.append(i*3)
    return a2

li = [1, 2, 3, 4]
li2 = times(li)
print(li2)

li2 = map(lambda x : x * 3, li)
print(list(li2))
'''
#7번

def find_max(li):
    max = li[0]
    for i in li:
        if max < i:
            max = i
    return max

    '''
    range를 통해서 범위를 지정하는 방법
    n = len(li)
    for i in range(1, n):
        print(max)
        if max < li[i]:
            max = li[i]   
    return max
    '''




d1 = [-8, 2, 7, 5, -3, 5, 0, 1]
max2 = find_max(d1)
'''
max = max(d1)
min = min(d1)
print(max)
print(min)

print(max + min)

간단한게 함수 쓰는 방법
'''

#8번

print(round(17/3, 4))

'''
n = 17 / 3
print("%.4f" % n)
'''

#9번

#myargv.py 참고

#10번

#os_ex.py 참고

#11번

#glob_ex.py 참고

#12번

import datetime

now = datetime.datetime.now()
print(now.strftime("%Y/%m/%d %H:%M:%S"))  #datetime 모듈

import time

now1 = time.strftime("%Y/%m/%d %H:%M:%S") #time 모듈
print(now1)

#13번

import random as r

lotto = []
while len(lotto) < 6:
    n = r.randint(1, 45)
    if n not in lotto: # --> 여기서 중복숫자가 방지된다. (n이 lotto에 포함되지 않아야 다음n을 추가한다)
        lotto.append(n)

print(lotto)

