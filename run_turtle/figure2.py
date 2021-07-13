# 도형그리기 (거북이)

import turtle as t # 별병 설정, 앞으로 t = turtle

t.shape("turtle")

#사각형 그리기
n = 4
for i in range(n):
    t.forward(200)
    t.right(360 / n)

#삼각형 그리기
t.color("red")
t.pensize(2)
n = 3
for i in range(n):
    t.forward(200)
    t. left(360 / n)


# 원 그리기
t.color("blue")
t.pensize(3)
t.circle(100)

# 별 그리기
t.color("pink")
t.pensize(4)
n = 5
for i in range(n):
    t.right(360 * 2 / n)
    t.forward(200)

t.mainloop()