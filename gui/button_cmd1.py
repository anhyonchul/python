from tkinter import *

def click():
    print("Hello Python")

root = Tk()
root.title("Hello~")   # --> 루트

frame = Frame(root)    # --> 프레임
frame.pack()

Button(frame, text="확인", command=click).grid(row=0, column=0)
# click()함수에서 ()를 생략한 이유는 버튼을 누를때만 작동시키려고
# ()가 있으면 함수 생성시점에서 동작해버림.



root.mainloop()
