#놀이공원 입장료 계산

age = int(input("나이를 입력해 주세요 : "))
charge = 0

if age < 8:
    print("취학 전 아동입니다.")
    charge = 1000
elif age < 14: # age >= 8 and age < 14 이렇게 할 필요가 없다
    print("초등학생 입니다.")
    charge = 2000
elif age < 20:
    print("중/고등학생 입니다.")
    charge = 3000
else:
    print("성인입니다.")
    charge = 5000

print("입장료는 %d원 입니다." % charge)
