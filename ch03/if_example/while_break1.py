#while ~ if break : 반복 조건문

i = 1
while True:
    print(i, end=' ')
    i = i + 1          #1씩 무한히 증가
    if i > 10:
        break        # 10보다 커지면 멈춘다.
    
