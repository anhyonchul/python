import os

'''
os.chdir("c:/")  #c:로 간다
dir = os.popen("dir")
print(dir)
print(dir.read())
'''

# 디렉터리 이름 - 리스트로 리턴 받기

dirnames = os.listdir("c:/pywork/exercise")
print(dirnames)
print(dirnames[0])
print(dirnames[-1])

for dirname in dirnames:
    print(dirname)   # 요소의 값 출력