#자연수 1부터 10까지 출력

i = 1
sum = 0
while i < 11:
    sum = sum + i #sum += i 와 같다.
    #print(i, end=' ')  #end=' ' 가로로 출력
    print("i = ", i, ", sum = ", sum)
    i += 1
    
print("합계 : ", sum)
