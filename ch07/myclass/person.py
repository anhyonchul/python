# Person 클래스 생성과 사용

class Person:
    def __init__(self):          # 초기자 (생성자함수)
        self.name = "안현철"
        self.age = 39

    def getname(self):           # 맴버변수에 직접 접근하지 않도록 get()을 사용한다.
        return self.name

    def getage(self):
        return self.age


p = Person()                      #객체변수 = 인스턴스(instance)
# p.name = "박바다"
# print(p.name, p.age)
print(p.getname(), p.getage())