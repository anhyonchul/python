
# indent(들여쓰기) - 4칸 : {}를 대체한다.

n = 10                  #자료형은 쓰지 않는다.  var let 같은거 다 생략이다.
if n % 2 == 0:          #파이썬은 세미콜론 ; 아니고 콜론 (:)
    print("짝수입니다")
    print("even")
else:
    print("홀수입니다")
    print("odd")

'''
#예시 : print 글자앞에 한칸만 띄워져도 에러남. 주의하자.

print('a')
print('b')
print('c')
'''

# 여러줄로 문자열 출력하기. 여러줄 주석처리와 혼동하지 말자
msg = '''
사과
귤
감
포도
'''
print(msg)
