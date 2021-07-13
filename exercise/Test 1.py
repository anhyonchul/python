# 시험 연습문제

#1
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in a:
    total = total + score
avg = total / len(a)
print(avg)

#2
num = [1, 2, 3, 4, 5]

result = []
for n in num:
    if n % 2 == 1:
        result.append(n * 2)

result = [n*2 for n in num if n % 2 == 1]
print(result)

#3

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value = self.value + val
        return self.value

# UpCal

class UpCal(Calculator):
    def sub(self, val):
        self.value = self.value - val
        return self.value

cal = UpCal()
cal.add(10)
cal.sub(7)
print(cal.value)


#4
class MaxLimCal(Calculator):
    def add(self, val):
        self.value = self.value + val
        if self.value > 100:
            self.value = 100
        return self.value

cal = MaxLimCal()
cal.add(50)
cal.add(60)
print(cal.value)

'''
배운대로 하면
'''
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

class UpCal(Calculator):
    def sub(self):
        return self.x - self.y

cal = UpCal(10, 7)
print(cal.sub())

class MaxLimCal(Calculator):
    def add(self):
        n = self.x + self.y
        if n > 100:
            n = 100
        return n

cal = MaxLimCal(50, 60)
print(cal.add())