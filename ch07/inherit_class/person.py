# person 클래스 - 맴버변수(name, age)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 상속 더하기 - Employee클래스는 Person을 상속받음

class Employee(Person):
    pass

if __name__ == "__main__":
    p1 = Person("안현철", 39)
    print(p1.name, p1.age)

    e1 = Employee("남한강", 30)
    print(e1.name, e1.age)