# 주민등록번호 뒷자리를 *처리 하는 방법

import re

data = """
    Ahn 831003-1234567
    lee 951011-2345678
"""
pat = re.compile("(\d{6})[-](\d{1})\d{6}")
m = pat.sub("\g<1>-\g<2>******", data)
print(m)