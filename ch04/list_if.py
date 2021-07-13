#리스트의 합격 판정
# 점수가 60점 이상이면 합격, 불합격

print("for - in 문 을 사용")
score = [72, 81, 53, 61, 98, 45]
index = 0

for i in score:
    index += 1
    if i >= 60: #여기서는 그냥 값 이기때문에 i로 쓴다.
        print("%d번 학생은 합격입니다" % index)
    else:
        print("%d번 학생은 불합격입니다" % index)

print("for - in rnage() 문 을 사용")

n = len(score)
for i in range(0,n): #range(1,n+1) 과 같다.
    if score[i] >= 60: #여기서는 리스트 안에서 값이기 때문에 i를 지정해준다.
            print("%d번 학생은 합격입니다" % (i+1))
    else:
        print("%d번 학생은 불합격입니다" % (i+1)) #대응변수는 괄호로 묶는다.
    
