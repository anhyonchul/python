#두수를 동시에 입력받아서 계산하기

#num1 = int(input("첫째수 입력 : "))
#num2 = int(input("둘째수 입력 : "))
#혹은

#num1 = input("첫째수 입력 : ")
#x = int(num1)
#num2 = input("둘째수 입력 : ")
#y = int(num2)

#print (num1, num2)
#add = num1 + num2
#혹은

#print (x, y)
#add = x + y

#print(add)

#원래는 위의 방식이지만

n1,n2 = input("두개의 수 입력 : ").split() #괄호안에 기호가 없으면 공백문자가 들어가있는것.
x = int(n1)
y = int(n2)

add = x + y
print(add)

#이렇게 가능

