"""
날짜 : 2021/02/25
이름 : 이승환
내용 : 교재 p151 - 함수와 클래스 예
"""
def calc_func(a,b):
    x = a
    y = b

    def plus():
        p = x + y
        return p

    def minus():
        m = x - y
        return m
    return plus, minus

p, m = calc_func(10,20)
print('plus =', p())
print('minus =', m())

class calc_class:
    x = y = 0

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def plus(self):
        p = self.x + self.y
        return p

    def minus(self):
        m = self.x - self.y
        return m

obj = calc_class(10, 20)

print('plus =',obj.plus())
print('minus =',obj.minus())
