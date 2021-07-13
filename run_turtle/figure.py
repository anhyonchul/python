# 도형그리기 (거북이)

import turtle as t # 별병 설정, 앞으로 t = turtle

t.shape("turtle")

#사각형 그리기
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)

#삼각형 그리기

t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)

# 원 그리기
t.circle(100)

t.mainloop()
