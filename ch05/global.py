# 전역변수(정적변수) 누적 공유되는 변수
# Global 키워드사용하기

# 1씩 증가하기

def one_up():
    global x  # ---> x를 전역변수로 쓰겠다는 의미
    x = x + 1
    return x  

x = 0
print(one_up())
print(one_up())
print(one_up())
print(one_up())
