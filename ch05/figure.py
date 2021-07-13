# 도형의 면적을 계산하는 함수

def square(w, h):
    area = w * h   # 따로 변수를 줘도 된다.
    return area

def triangle(n, h):
    area = (n * h) / 2
    return area

print('사각형의 면적 : %.f cm' % square(5, 4))
print('삼각형의 면적 : %.f cm' % triangle(4, 7))

# print(area) 하면 안된다. 
