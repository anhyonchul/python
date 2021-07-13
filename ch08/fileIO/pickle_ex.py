import pickle
# 객체의 형태를 그래도 저장하고 불러오는 모듈
# 바이너리 모드 사용한다.

with open('data2.txt', 'wb') as f:
    li = ['강아지', '고양이', '닭']
    dic = {1:'사과', 2:'딸기', 3:'수박'}
    pickle.dump(li, f)
    pickle.dump(dic, f)

with open('data2.txt', 'rb') as f:
    li = pickle.load(f)
    dic = pickle.load(f)
    print(li)
    print(dic)