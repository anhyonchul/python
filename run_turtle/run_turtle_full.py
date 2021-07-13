
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

def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        play()

def message(m1, m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 15))
    t.home()


def play():
    global score
    global playing

    t.forward(10)               #주인공 거북이 속도

    if random.randint(1, 5) == 3:   # 3d을 뽑을 확율이 20%
        ang = te.towards(t.pos())   # 적 거북이가 쫒아온다.
        te.setheading(ang)

    speed = score + 5           # 적거북이 초기속도5, 점수1점마다 속도가 1씩 추가된다.
    te.forward(speed)

    if t.distance(tf) < 12:     # 주인공이 먹이를 먹으면 점수가 1 올라간다. 먹이는 랜덤생성
        score = score + 1
        t.write(score)
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        tf.goto(x, y)

    if t.distance(te) < 12:      # 잡히면 게임오버
        text = "Score : " + str(score)
        message("Game Over", text)
        playing = False
        score = 0

    if playing:
        t.ontimer(play, 100)


#메인

#점수변수와 플레이 스위치(bull) 변수 선언
score = 0
playing = False


t.setup(600, 600)
t.title("Run, Turtle, Run")


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

t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")
t.listen()
message("Run, Turtle, Run", "[spacekey] to Start")

t.mainloop()
