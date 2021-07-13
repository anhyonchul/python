
# 파일 열기 -> 파일 쓰기 -> 파일 닫기
# open() ---> write() -> close()

f = open('c:/pyfile/hello.txt', 'w')
f.write("hello! python!!\n")
#f.write(1000)  #--> 숫자를 바로 쓰면 오류
f.write("%d \n" % 100) # --> 숫자는 바로 입력불가, 포맷 방식으로 입력하면 된다.
f.write("%.1f \n" % 7.3)
num = "%d \n" % 100000
f.write(num)
f.write("안녕~ 파이썬\n")
f.close()