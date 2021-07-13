# 학생 클래스 생성과 사용

class Student:
    def __init__(self,school, sid, name):
        self.school = school
        self.sid = sid
        self.name = name

    def getschool(self):
        return self.school

    def getsid(self):
        return self.sid

    def getname(self):
        return self.name

if __name__ == "__main__":  #이건 여기서만 실행되게 한다. 다른파일에서 클래스를 불러도 아래는 표시 안됨.
    s1 = Student("경기대학교", 200230145, "안현철")
    s2 = Student("경기대학교", 200230120, "조선익")
    print(s1.getschool(), s1.getsid(), s1.getname())
    print(s2.getschool(), s2.getsid(), s2.getname())