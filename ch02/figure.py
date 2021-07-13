#도형의 넓이 계산하기

# 정사각형의 넓이

size = int(input("정사각형 한변의 길이는 : "))
area = size*size
#print("정사각형의 넓이 : ", area,"cm") 이렇게 하면 숫자와 cm 사이에 간격이 생김
print("정사각형의 넓이 : %dcm" % area)

# 삼각형의 넓이
width = int(input("삼각형의 밑변의 길이는 : "))
heigth = int(input("삼각형의 높이는 : "))
area = (width * heigth) / 2
print("삼각형의 넓이 : "  ,area , "cm")
print("삼각형의 넓이 : %dcm" % area)


number = 4
print("I eat %d grapes" % number) #정수일때는 %d

print("I eat %s bananas" % "five") #문자일때는 %s

print("1인치는 %.2fcm 입니다." % 2.54) #소수일때는 %f, %.2f하면 소수점 둘째자리까지

