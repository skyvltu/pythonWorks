"""
날짜 : 2025/02/25
이름 : 이승환
내용 : 교재 p161 - 캡슐화 예
"""
class account:
    __balance = 0
    __accname = None
    __accno = None

    def __init__(self, bal, name, no):
        self.__balance = bal
        self.__accname = name
        self.__accno = no

    def getbalance(self):
        return self.__balance, self.__accname, self.__accno

    def deposit(self, money):
        if money < 0:
            print('금액 확인')
            return
        self.__balance += money

    def withdraw(self, money):
        if self.balance < money:
            print('잔액 부족')
            return
        self.__balance -= money

acc = account(1000, '홍길동', '125-152-4125-41')

acc.__balance
bal = acc.getbalance()
print('계좌정보 : ', bal)

acc.deposit(10000)
bal = acc.getbalance()
print('계좌정보 : ', bal)