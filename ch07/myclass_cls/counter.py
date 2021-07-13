# Counter Class

# 인스턴스변수 사용

class Counter:
    def __init__(self):
        self.x = 0    # 인스턴서 변수 (heap 영역)
        self.x = self.x + 1

    def showinfo(self):
        print(self.x)

c1 = Counter()
c1.showinfo()
c2 = Counter()
c2.showinfo()
c3 = Counter()
c3.showinfo()


print()

# Counter Class 클래스변수 사용

class Counter:
    x = 0            # 클래스변수 - 클래스안에 있다

    def __init__(self):
        Counter.x = Counter.x + 1     # 변수가 위에 있으므로 이것도 바뀐다.

    def showinfo(self):
        print(self.x)

c1 = Counter()
c1.showinfo()
c2 = Counter()
c2.showinfo()
c3 = Counter()
c3.showinfo()