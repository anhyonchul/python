# 로또복권 번호 생성 프로그램

import random as r

lotto = [] # 빈 리스트
'''
lotto.append(45) # 리스트에 45를 추가한다.
print(lotto) 원래 추가는 이런식이지만 그걸 랜덤으로 하면
'''
'''
for x in range(6):
    n = r.randint(1, 45)
    if n not in lotto: # (2) 중복을 제외함 / 하지만 중복제외를 하니 숫자가 5개밖에 안나온다.
        lotto.append(n)  # (1) 6개의 숫자 랜덤 추출 /  하지만 중복이 된다.
    #if len(lotto) == 6: 
        #break

print(lotto)
'''

# 그래서 while문을 쓴다
lotto2 = []
while len(lotto2) < 6: # 결과가 6개가 될때까지
    n = r.randint(1, 45)
    if n not in lotto2: 
        lotto2.append(n)

print(lotto2)
