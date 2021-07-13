#이차원 리스트의 생성과 출력

# li = [[10,  20], [30, 40], [50, 60]] 이건

li = [
        [10,  20],
        [30, 40],
        [50, 60]
      ]
#이렇게 배열이 되었다고 생각하면 된다.

print('li[0][0] =', li[0][0])
print('li[0][1] =', li[0][1])

print('li[1][0] =', li[1][0])
print('li[1][1] =', li[1][1])

print('li[2][0] =', li[2][0])
print('li[2][1] =', li[2][1])

print("리스트(행)의 크기 : ", len(li))

for i in range(len(li)):
    #print(len(li[i]))
    for j in range(len(li[i])):
        print(li[i][j], end = " ")
    print()
'''
for x, y in li:
    print(x, y)
와 같다. 파이썬만 가능.
'''

