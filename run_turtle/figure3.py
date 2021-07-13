# 여러개의 원 만들기
import turtle as t

n = 50
t.speed(0)   # 0~9까지 있고 0이 가장 빠르다.
t.color("white")
t. pensize(2)
t.bgcolor("black")

for x in range(n):
    t.circle(200)
    t.left(360 / n)

t.mainloop()