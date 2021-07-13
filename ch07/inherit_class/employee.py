# 맴버 매개변수가 있는 상속

from person import Person  #person.py의 Person class를 상속한다.

class Employee(Person):
    def __init__(self, name, age, empid):  # name 과 age를 안쓰면 오류.
        super().__init__(name, age)        # 부모의 매개변수 name과 age를 가져온다는 함수 super()를 쓴다.
        self.empid = empid

e1 = Employee("안현철", 39, 200230145)
print(e1.name, e1.age, e1.empid)

e2 = Employee("아롱이", 13, 2009)
print(e2.name, e2.age, e2.empid)