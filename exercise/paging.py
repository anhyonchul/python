# 게시판 페이징 하기

def getpage(x, y):
    if x % y == 0:
        return x // y
    else:
        return (x // y) + 1

print("필요한 게시판 페이지의 수는 :",getpage(5, 10),"개 입니다")
print("필요한 게시판 페이지의 수는 :",getpage(10, 10),"개 입니다")
print("필요한 게시판 페이지의 수는 :",getpage(15, 10),"개 입니다")
print("필요한 게시판 페이지의 수는 :",getpage(25, 10),"개 입니다")
print("필요한 게시판 페이지의 수는 :",getpage(35, 10),"개 입니다")