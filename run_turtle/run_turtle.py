
import turtle as t
import random

# 함수

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def play():
    t.forward(10)
    te.forward(9)

    # 적 거북이가 주인공 거북이를 쫒아감.
    ang = te.towards(t.pos())
    te.setheading(ang)

    # 주인공 거북이가 먹이에 닿으면 먹이를 랜덤하게 이동시키기
    if t.distance(tf) < 12:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        tf.goto(x,y)

    if t.distance(te) >= 12:    # 적거북이와 거리가 12픽셀보다 커야 게임이 진행된다. 즉 작으면 멈춘다.
        t.ontimer(play, 100) # 0.1초당 1


#메인

t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")

# 내 거북이 설정
t.bgcolor("bisque")
t.shape("turtle")
t.speed(0)
t.up()
t.color("blue")

#적 거북이 설정
te = t.Turtle() # Turtle() 클래스에서 te인스턴스 생성
te.shape("turtle")
te.color("red")
t.speed(0)
te.up()
te.goto(0, 200)

#먹이 설정
tf = t.Turtle()
tf.shape("circle")
tf.color("green")
tf.speed(0)
tf.up()
tf.goto(0, -200)

t.listen()
play()
t.mainloop()
