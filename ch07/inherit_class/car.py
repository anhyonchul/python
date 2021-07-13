# Car 클래스 - Taxi, Bus가 자식클래스
# 상속의 경우 매소드 재정의
class Car:
    def drive(self):
        print("자동차가 주행합니다.")

class Taxi(Car):
    def drive(self):
        print("택시가 주행합니다.")   # 부모의 매소드를 상속받았지만, 재정의 되어서 본인게 출력된다.

class Bus(Car):
    def drive(self):
        print("버스가 주행합니다.")

c = Car()
c.drive()

t = Taxi()
t.drive()

b = Bus()
b.drive()
