# 파일을 리스트형태로 읽어오는 readline

with open("2021kbo.txt", 'w') as f:
    team = ["KIA Tigers","Samsung Lions","LG Twins","NC Dinos","SSG Landers","Hanwha Eagles","Lotte Giants"]
    for i in team:
        f.write(i + '\n')

with open("2021kbo.txt", 'r') as f:
    #data = f.readlines()  # 파일읽기의 결과를 리스트로 보여준다
    #print(data)
    '''
    for i in range(7):
        data = f.readline().split()  # 리스트형태로 하나씩 끊을때 쓴다.
        print(data)
    '''

    # 2차원 리스트로 담기
    d2 = [] # 새 리스트 준비
    for i in range(7):
        d2.append(f.readline().split())
    print(d2)