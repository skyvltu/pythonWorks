"""
날짜 : 2021/02/25
이름 : 이승환
내용 : 교재 p159 - 클래스 멤버 예
"""
class datepro:
    content = "날짜 처리 클래스"

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def display(self):
        print("%d-%d-%d"%(self.year, self.month, self.day))

    @classmethod
    def date_string(cls, datestr):
        year = datestr[:4]
        month = datestr[4:6]
        day = datestr[6:]

        print(f"{year}년 {month}월 {day}일")

date = datepro(1995,10,25)
print(date.content)
print(date.year)
date.display()