# set() 집합자료구조의 특징
# 순서가 없고, 중복이 허용되지않는다.

s = set() # 빈 집합자료형 선언

s.add(1)
s.add(2)
print(s)

s2 = set(['cow', 'dog', 'cat', 'dog'])
print(s2)  # ---> 중복이 허용되지 않으므로 'dog'는 한개만 출력, 순서도 없음


#리스트와 비교
#리스트는 당연히 인덱스로 찾아야 하기때문에 순서도 지켜지고 중복도 허용됨.

ani = ['cow', 'dog', 'cat', 'dog']
print(ani)
