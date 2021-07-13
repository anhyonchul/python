# 영타 연습 프로그램

import random
import time

f = open("word.txt", 'r')
word = f.read().split()   # --> 리스트형태로 자료를 가져옴
#print(word)
f.close()

n = 1  # 문제번호
print("[Typing Game] Ready To [ENTER]key")
input()

start = time.time()

q = random.choice(word) # 단어 랜덤 선택

while n <= 10:
    print("문제", n)
    print(q)
    x = input()  # 사용자가 단어를 따라서 입력
    if q == x:
        print("통과")
        n = n + 1
        q = random.choice(word)
    else:
        print("오타! 다시 도전하세요")
    #n = n + 1  # --> 여기 들어가면 오타가 나도 10번안에 끝남.

end = time.time()
et = end - start
print("게임이 종료되었습니다. \n총 걸린 시간은 : %.2f초 입니다." % et)