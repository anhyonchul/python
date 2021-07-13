# 딕셔너리
'''
>>> person={}
>>> person['name'] = "마이클조던"
>>> person
{'name': '마이클조던'}
>>> person['age'] = 30
>>> person
{'name': '마이클조던', 'age': 30}
>>> person['phone'] = '010-1234-5678'
>>> person
{'name': '마이클조던', 'age': 30, 'phone': '010-1234-5678'}
>>> del person['phone']     삭제
>>> person
{'name': '마이클조던', 'age': 30}
>>> person['age'] = 25        수정
>>> person
{'name': '마이클조던', 'age': 25}
>>> person.keys()        키값 보여주기
dict_keys(['name', 'age'])
>>> 


>>> dic = {1: "사과", 2: "귤", 3: "바나나"}  직접 전부입력
>>> dic.keys()  ---> 키값
dict_keys([1, 2, 3])
>>> dic.values() ---> 벨류값
dict_values(['사과', '귤', '바나나'])
>>> dic[4] = "감"   ---> 리스트에 추가
>>> dic
{1: '사과', 2: '귤', 3: '바나나', 4: '감'}
>>> del dic[2] ---> 리스트 삭제
>>> dic
{1: '사과', 3: '바나나', 4: '감'}
>>> dic.pop(1)  ---> POP를 이용한 삭제
'사과'
>>> dic
{3: '바나나', 4: '감'}
>>> dic[1] = "포도"
>>> for i in dic:      ---> 리스트 상태가 아니라 값만 알고 싶을떄
	print(dic[i])

	
바나나
감
포도
'''
