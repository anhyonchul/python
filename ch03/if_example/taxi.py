#조건이 있는 if else
#조건 = 현금이 있고, 카드가 있으면 택시를 타고, 아니면 걸어간다.

cash = 3000
card = True

if cash > 4000 or card: #둘중 하나만 True면 됨. 카드가 있으므로 택시탐.
    print("택시를 탄다")
else:
    print("걸어 간다")


if cash > 4000 or not card: #둘다 False이기 때문에 걸어감.
    print("택시를 탄다")
else:
    print("걸어 간다")


if cash > 4000 and card: #두개 모두 True 여야 됨. 걸어감
    print("택시를 탄다")
else:
    print("걸어 간다")


pocket = ['paper', '스마트폰', 'money']
if 'money' in pocket:
    print("택시를 탄다")
else:
    print("걸어간다")
    
#리스트중에 하나라도 걸리면 True
