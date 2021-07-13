#나이 계산 프로그램

currentYear = 2021

birthYear = int(input("태어난 연도를 입력하세요 : "))
age = currentYear - birthYear + 1
print("%d년에 태어난 당신의 나이는 %d세 입니다"  % (birthYear, age))
