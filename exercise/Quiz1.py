#1번

국어 = 80
영어 = 75
수학 = 55

sum = 국어 + 영어 + 수학
avg = sum / 3

print("홍길동씨의 평균점수는 %d점 입니다" % avg)

#2번 홀수인지 짝수인지 판별할 수 있는 방법

num = int(input("숫자를 입력하세요 : "))
if num / 2 == 0:
    print("자연수 %d은(는) 짝수입니다." % num)
else:
    print("자연수 %d은(는) 홀수입니다." % num)

#3번과 4번

pin = "881120-1068234"
yyyymmdd = pin[0:6]
print(yyyymmdd)
num = pin[7:]
print(num)

gender = pin[7]
# print(gender)
if gender =="1": #여기선 문자이기때문에 ""을 꼭 해준다. 아닐시 int를 써야됨.
    print("남자입니다")
else:
    print("여자입니다")


#5번
a = "a:b:c:d"
b = a.replace(":", '#')
print(b)

#6번
a = [1,3,5,4,2]
a.sort()
print(a)
a.reverse()
print(a)

#7번 join
a = ['Life', 'is', 'too', 'short']
result = " ".join(a) #" "로 빈 문자열을 만들어야 한다.
print(result)
#7-1 split
s = "Life is too short"
s = s.split() # 구분기호는 공백
print(s)

msg = "a:b:c:d"
msg = msg.split(':')
print(msg)

#8번
a = (1,2,3)
a = a + (4,)
print(a)

#9번
a = dict()
print(a)

a['name'] = 'python'
print(a)
a[('a')] = 'python'
print(a)
#a[[1]] = 'python'   ---> 
#print(a)
a[250] = 'python'
print(a)

#10번
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

#11번
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a) # 중복이 제거(튜플자료형)
b = list(aSet) # 다시 리스트형으로 변환
print(b)

#12번
a = b = [1,2,3]
a[1] = 4
print(b) #a와 b의 변수가 동일하기때문에
