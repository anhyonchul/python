import turtle as t
import random

t.shape("turtle")
t.speed(0)
t.up()
# t.goto(0, -300) 위치를 잡는 함수
x = random.randint(-300, 300)   #랜덤 좌표 설정
y = random.randint(-300, 300)
t. goto(x, y) # 랜덤한곳에 생성


t.mainloop()