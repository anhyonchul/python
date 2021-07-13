# 다른곳에 도형 그리기

import turtle as t
t.shape("turtle")

def polygon(n):
    for x in range(n):
        t.forward(50)
        t.left(360 / n)

def polygon2(n, d):  #매개변수 2개넣기 (n 변의 갯수, d 길이)
    for x in range(n):
        t.forward(d)
        t.left(360 / n)
        
polygon(3)
polygon(5)

t.up()  # 선 올리기
t. forward(100)  # 200픽셀만큼 뒤로 이동
t.down() # 선 내리기

polygon2(4, 80)
polygon2(5, 80)
'''
for x in range(3):
    t.back(200)
    t.right(120)

t.up()
t.right(90)
t.forward(250)
t.down()

n = 5
for i in range(n):
    t.right(360 * 2 / n)
    t.forward(200)

t.up()
t.left(90)
t.forward(250)
t.down()

n = 5
for i in range(n):
    t.right(360 * 2 / n)
    t.forward(200)
'''

t.mainloop()