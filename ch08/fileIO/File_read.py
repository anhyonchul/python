
try:
    f = open('c:/pyfile/hello.txt', 'r')
    data = f.read()
    print(data)  # --> 파일에 있는것을 콘솔창에 출력
    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

