# Calculator를 상속받아서 확장한 업그래이드 클래스 만들기

from ch07.myclass.calculator import Calculator

class MoreCalculator(Calculator):
    def pow(self):
        return self.x ** self.y   # 제곱수 구하는 함수 추가

    def div(self):
        if self.y == 0:
            return 0
        else:
            return self.x / self.y  # 0을 나누면 오류나던것을 수정

c = MoreCalculator(15, 0)
print(c.pow())
print(c.add())
print(c.sub())
print(c.mul())
print(c.div())