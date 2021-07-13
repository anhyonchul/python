
# 웹 스크레이핑 (크롤링)

from urllib import request

#url = "http://naver.com"
content = request.urlopen("http://daum.net")
print(content.read())