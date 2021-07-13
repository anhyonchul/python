# 자리 배치도 프로그램 - 나누기와 나머지를 이해 할 수 있어야 함

costomer_num = int(input("입장객 수 입력 : "))
col_num = int(input("좌석 열의 수 입력 : "))

if costomer_num % col_num == 0:
    row_num = int(costomer_num / col_num) #나머지는 결과가 실수이므로 정수로 형변환 해줘야 한다.
else:
    # row_num = int(costomer_num / col_num + 1)
    row_num = costomer_num // col_num + 1

print("%s개의 줄이 필요합니다." % row_num)

print("자리 배치도")
for i in range(0, row_num):
    for j in range(1, col_num + 1):
        seat_num = i * col_num + j
        print(seat_num, end=" ")
        if seat_num == costomer_num:
            break
    print()
