"""
날짜 : 2021/02/25
이름 : 이승환
내용 : 교재 p157 - self 명령어 예
"""
class multiply3:

    def data(self, x, y):
        self.x = x
        self.y = y

    def mul(self):
        result = self.x * self.y
        self.display(result)

    def display(self, result):
        print("곱셈 = %d" %(result))

obj = multiply3()
obj.data(10, 20)
obj.mul()
