"""
날짜 : 2021/03/11
이름 : 이승환
내용 : 파이썬 연습문제 9. 클래스
"""

class king:

    def __init__(self, name='태조', year=1392):
        self.name = namme
        self.year = year

    def show(self):
        print('---------------')
        print('name :', self.name)
        print('year :', self.year)

if __name__ == '__main__':

    king1 = king()
    king2 = king('태종')
    king3 = king('세종대왕', 1418)

    king1.show()
    king2.show()
    king3.show()