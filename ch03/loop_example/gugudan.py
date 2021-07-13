#구구단 출력하기

dan = int(input("숫자를 입력해주세요(1~9) : "))
          
for i in range(1, 10):
    print("%d x %d = %d" % (dan, i, dan*i))
