

def incrementor(n):
    return lambda x : x + n

f = incrementor(10)
print(f(1))    # --> 이건 람다함수의 매개변수.
print(f(2))