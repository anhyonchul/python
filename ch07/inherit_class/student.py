# Student 클래스 - 학번(stuid)

from person import Person

class Student(Person):
    def __init__(self, name, age, stuid):
        super().__init__(name, age)
        self.stuid = stuid

    def showinfo(self):
        print(self.name, self.age, self.stuid)




s1 = Student("손흥민", 30, 2021101)
s1.showinfo()
s2 = Student("박지성", 40, 2011100)
s2.showinfo()