
#1차원 리스트 복습

d1 = [1, 2, 3]
print(d1[0])
d1.append(10)   # 10추가
print(d1)


#2차원 리스트 이해

d2 = [
      [10],
      [20],
      [30]
      ]
'''
print(d2[0][0]) # = 10
print(d2[1][0]) # = 20
print(d2[2][0]) # = 30
'''
# 즉 이건 3행 1렬짜리 리스트다.

d2.append([40]) # 리스트 형식으로 추가.
#print(d2)

for i in d2:
    print([i][0])

# 리스트의 연산

d2.append([d2[0][0] + d2[1][0] + d2[2][0] + d2[3][0]]) # 합계를 리스트형태로[]로 묶어서 추가
print(d2)

avg = (d2[0][0] + d2[1][0] + d2[2][0] + d2[3][0]) / 4  # 평균을 리스트형태[]로 묶어서 추가
d2.append([avg])
print(d2)