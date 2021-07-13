# 온도변환기 app


from tkinter import *

# 온도변환기 클래스에서 가져온다.
from gui.converters import Converters

class App:
    def __init__(self, master):
        self.conv = Converters('C', 'F', 1.8, 32)

        #프레임 만들기
        frame = Frame(master)
        frame.pack()

        #라벨 만들기
        Label(frame, text='섭씨 C').grid(row=0, column=0)
        self.c = DoubleVar()   # 실수형 변수 선언
        Entry(frame, textvariable=self.c).grid(row=0, column=1)

        Label(frame, text='화씨 F').grid(row=1, column=0)
        self.f = DoubleVar()
        Label(frame, textvariable=self.f).grid(row=1, column=1) # 여기는 입력이 아니므로 엔트리가 아니라 출력용 레이블

        #버튼 만들기
        Button(frame, text="변환", command=self.convert).grid(row=2, columnspan=2)

    def convert(self):
        c = self.c.get()  # 섭씨 c의 값 가져오기
        c_to_f = str(self.conv.convert(c))[0:5] # converter.py에 convert함수를 바로 불러옴, c -> f로 변환
            # 문자형으로 변환          #소수점 둘째자리까지 표현.
        self.f.set(c_to_f) # 화씨 f 에 넣어준다.


root = Tk()
root.title("온도변환기")
app = App(root)



root.mainloop()