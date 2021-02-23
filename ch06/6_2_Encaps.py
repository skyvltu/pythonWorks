"""
 날짜 : 2021/02/23
 이름 : 이승환
 내용 : 파이썬 객체지향 캡슐화 실습하기 교재 p161
"""
from ch06.lib.Account import Account
from ch06.lib.Calc import Calc
from ch06.lib.Person import Person

kb = Account('국민은행', '121-11-1234', '김유신', 10000)

kb.bank = '국민은행'
kb.id = '122-11-1234'
kb.name = '김유신'
kb.money = 10000

kb.deposit(20000)
kb.withdraw(3000)
kb.money -= 1

kb.show()

wr = Account('우리은행', '111-10-1021', '김춘추', 20000)
wr.deposit(30000)
wr.withdraw(5000)
wr.show()

# 연습문제
Calc = Calc()

r1 = Calc.plus(1, 2)
r2 = Calc.minus(1, 2)
r3 = Calc.multi(2, 3)
r4 = Calc.div(4, 2)

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)
print('r4 :', r4)

kim = Person('김유신', 25)
kim.hello()

lee = Person('이순신', 35)
lee.hello()
