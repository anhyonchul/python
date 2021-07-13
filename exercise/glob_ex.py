import glob

data = glob.glob("c:/pywork/exercise/*.py")  # 리스트 형식으로 출력
print(data)

print(data[0])
print(data[-1])

for i in data:
    print(i)    # 요소값을 하나씩 출력