# 단위 변환 클래스

class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor

    def convert(self, val):  #self.factor : 25
        return self.factor * val


c1 = ScaleConverter("inches", "mm", 25)
print("Conterting to inches")
print(str(c1.convert(9)) + c1.units_to)
