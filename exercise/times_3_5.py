# 3과 5의 배수의 합

num = 0
for i in range(1, 11):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        num = num + i
print("3과 5의 배수의 합은 %d 입니다 " % num)