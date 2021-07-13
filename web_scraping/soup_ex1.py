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
soup = BeautifulSoup(html_str, "html.parser")
#print(soup)
ul = soup.find('ul')    # find()는 맨처음 나오는 태그만 검색
print(ul)
print(ul.text)      # 태그를 빼고 검색