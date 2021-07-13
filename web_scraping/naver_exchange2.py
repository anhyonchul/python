
from urllib import request
from bs4 import BeautifulSoup

html = request.urlopen('https://finance.naver.com/marketindex/')
code = html.read().decode('euc-kr', 'replace').encode('utf-8', 'replace')
contents = BeautifulSoup(code, 'html.parser')
lis = contents.select("ul.data_lst li") # find가 아닌 select를 사용하는 방법. (태그이름.클레스이름 :는 안쓴다)
# find와는 다르게 ul을 다 찾아오기 때문에 결과값이 find보다 많이 나온다.

for li in lis:
    ex = li.select_one("span.blind")
    val = li.select_one("span.value")
    #print(ex)
    #print(val)
    print(ex.string.split(' ')[-1], ':' ,val.string)