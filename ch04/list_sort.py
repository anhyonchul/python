# 리스트의 최대,최소값

score = [70, 80, 50, 60, 90, 45]
max = score[0]
min = score[0]
n = len(score)   #6

score.sort() # --> 간단한 오름차순 방법
print(score)

for i in range(1, n):
    if score[i] > max:
        max = score[i]

print("최고 점수는 %d점 입니다." % max)

for i in range(1, n):
    if score[i] < min:
        min = score[i]
print("최저 점수는 %d점 입니다." % min)


#리스트를 오름 차순으로 다시 정렬

for i in range(0, n):  
    for j in range(0, n-1):
        if score[j] > score[j + 1]:
            score[j], score[j+1] = score[j+1], score[j]

            '''
              # 1행
                  70 50 60 80 45 90
                  70 80 비교 이동X, 80 50 비교 이동 ,80 60 비교 이동, 80 90 비교 이동X, 90 45비교 이동X
              # 2행
                 50 60 70 45 80 90
              # 3행
                 50 60 45 70 80 90
              # 4행
                 50 45 60 70 80 90
              # 5행
                 45 50 60 70 80 90
            '''

for i in score:
    print(i, end=' ')
