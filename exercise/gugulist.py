# 구구단 곱한 값 리스트

def gugu(dan):
    li = []

    for i in range(1, 10):
        li.append(dan * i)
        #print(li)
    return li

print(gugu(2))