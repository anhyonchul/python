
with open("scorelist.txt", 'r') as f:
    d2 = []   # 이차원 리스트 준비
    for i in range(3):
        d2.append(f.readline().split())
    #print(d2)
    '''
    [
        ['이순신', '100', '95'], 
        ['원균', '45', '50'], 
        ['이연', '75', '65']
    ]
    '''
    for i in range(3):
        d2[i][1] = int(d2[i][1])    # 국어점수를 숫자형으로 변환  2열
        d2[i][2] = int(d2[i][2])    # 수학점수를 숫자형으로 변환  3열
        d2[i].append(d2[i][1] + d2[i][2])    #총점을 추가      4열
        d2[i].append(d2[i][3] / 2)           #평군을 추가      5열

    print(" ---------- 성 적 표 ---------- ")
    print(" ============================= ")
    print(" 이름   국어   수학   총점   평균  ")

    for i in range(3):
        print(" {}  {}    {}    {}   {} ".format(d2[i][0], d2[i][1], d2[i][2], d2[i][3], d2[i][4]))
    print(" ============================= ")
    print(" --------- 과목별 평균 --------- ")
    kor_sum = 0
    math_sum = 0
    for i in range(3):
        kor_sum += d2[i][1]
        math_sum += d2[i][2]
    print(" * 국어 : %.1f점 * 수학 : %.1f점" % (kor_sum / 3, math_sum / 3))