# 랜덤하게 거북이 걸어가기

import turtle as t
import random as r

t.shape("turtle")
t.speed(0)
t.bgcolor("pink")
t.pensize(3)
t.color("white")
t.setup(600, 600) #작업영역(윈도우창)의 크기

for x in range(1000):   #()번 반복
    angle = r.randint(1, 360) # 거북이 머리 각도를 랜덤
    t.setheading(angle) # 거북이의 방향을 각도로 조정
    t.forward(20)

t.mainloop()