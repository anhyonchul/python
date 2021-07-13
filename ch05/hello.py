# 함수의 정의 및 호출

# 1. return이 없고 매개변수가 없는 함수

def say_hello():
    print("안녕하세요")

# 2. return이 없고 매개변수가 있는 함수 (함수는 함수끼리 배치)

def say_hello2(name):
    print("{}님 반갑습니다.".format(name))

say_hello()  # 1. 호출
say_hello()
print('='*30)

say_hello2('손흥민')  # 2. 호출
say_hello2('shawn Michaels')
