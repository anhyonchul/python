
from urllib import request
from bs4 import BeautifulSoup

html = request.urlopen("https://www.naver.com/")
contents = BeautifulSoup(html, 'html.parser')

div = contents.find('div', {'class':'service_area'})  #div중 클래스=service_area 를 찾음
print(div)

a = div.find('a') # 위 div중에 a를 찾음

print(a)   # 전체 태그
print(a.text)  # 택스트만