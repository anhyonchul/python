
def vartest(a):
    #global a 라고 선언하면 같아진다.
    a = a + 1 # 지역변수 a
    return a

a = 1 # 전역변수 a
print(vartest(a))  # --> 이건 Return a 라고 보면되고 지역변수의 a
print(a)           # --> 이건 a = 1에 a다. 즉 전역변수의 a
