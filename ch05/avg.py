# 리스트를 매개변수로 전달하기

# 점수의 평균

def avg(a):
    sum = 0
    c = len(a) # 리스트 값의 개수

    for i in a:
        sum = sum + i
        print("i=%d, sum=%d" % (i, sum))
    avge = sum / c
    print('학생수는 %.f명 입니다' % c)
    return avge

korean = [70, 80, 90, 60, 100, 50]
avg = avg(korean)

print("평균점수는 %.1f점 입니다" % avg)
