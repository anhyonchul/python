
# 파일 입력받아 쓰기

f = open('input.txt', 'a')
text = input("내용을 입력하세요 : ")
f.write(text)
f.write('\n')
f.close()

