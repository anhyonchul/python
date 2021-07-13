'''
#1번


def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

print(is_odd(3))
print(is_odd(4))


#2번 파이썬에만 있는 기능, 가변매개변수

def avg_num(*args):  #*args = 모든 args를 포함한다.
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_num(1,2))
print(avg_num(1,2,3,4,5))


#3번

input1 = int(input("첫번째 수를 입력하세요 : "))
input2 = int(input("두번째 수를 입력하세요 : "))

total = input1 + input2
print("두수의 합은 %.f 입니다" % total)

#4번

print("you" "need" "python")
print("you" + "need" + "python")
print("you", "need", "python")
print("".join(["you" "need" "python"]))  #join내장 함수는 리스트에 나누어져 있는것을 다 연결해준다.


#5번

f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()


#6번

user_input = input("저장할 내용을 입력하세요 : ")
f = open('test.txt','a')
f.write(user_input)
f.write('\n')
f.close()
'''

#7번
f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open("test.txt", 'w')
f.write(body)
f.close()
