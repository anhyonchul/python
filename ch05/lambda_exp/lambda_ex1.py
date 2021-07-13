# 매개변수가 1개인 람다식 (익명함수)

# 1씩 증가하는 함수
oneup = lambda x : x + 1

def oneup2(x):
    return x + 1   # 원래 배웠던 방식은 이거


print(oneup(1))  # --> 람다함수 출력
print(oneup2(2)) # --> 일반함수 출력

print((lambda x : x + 1)(3))  # --> 람다함수를 한번에 출력, 이렇게 쓰는 경우가 많음.

# 3의 배수

threeTimes = lambda n : n * 3
print(threeTimes(3))

print((lambda n : n * 3)(2))    # --> 같은 방식. 한번에 출력