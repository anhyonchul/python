#문자열 인덱싱과 슬라이싱

#indexing은 무엇인가를 가리킨다 는 의미
#slicing은 무엇인가를 잘라낸다는 의미
#인덱싱은 0부터 시작한다.

say = "Have a nice day!"
#      0123 4 5678 9101112

say[0] # H
say[-1] #! -1은 마지막
say[-2] # y
say[0:3]# 'Hav'
say[0:4] # 'Have'
say[7:] # nice day!
len(say) #16
