# BeautifulSoup 모듈 사용하기

from bs4 import BeautifulSoup

html_str='''
<html>
<body>
    <ul class='item'>
        <li>인공지능</li>
        <li>빅데이터</li>
        <li>로봇</li>
    </ul>
        <ul class='leng'>
        <li>한국어</li>
        <li>영어</li>
        <li>일본어</li>
    </ul>
</body>
</html>
'''

contents = BeautifulSoup(html_str, 'html.parser')
ul = contents.find('ul', {'class':'leng'})  # {} = 딕셔너리구조 {class값 : 키값} 으로 해서 검색한다.
print(ul)

li = ul.find('li')  # 가장 상위의 리스트만 검색됨.
print(li)

# 마지막인 일본어를 검색하려면???

lis = ul.find_all('li')  # 리스트형태로 전부 검색됨.
print(lis)
print(lis[2].text)