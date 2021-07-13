from urllib import request
from bs4 import BeautifulSoup

html = request.urlopen('https://finance.naver.com/marketindex/')
code = html.read().decode('euc-kr', 'replace').encode('utf-8', 'replace')
contents = BeautifulSoup(code, 'html.parser')
ul = contents.find('div', {"class":"market_data"})
lis = ul.find_all('li')

for li in lis:
    ex = li.find('span', {'class':'blind'}) # 환율 종류
                # <span class="blind">미국 USD</span> 네이버상 이렇게 태그가 되어있음
    val = li.find('span', {'class':'value'}) # 환율 지수
    #print(ex)
    #print(val)
    print(ex.string.split(' ')[-1], ':' ,val.string)