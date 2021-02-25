"""
날짜 : 2021/02/25
이름 : 이승환
내용 : 교재 p166 - super 예
"""
class parent:

    def __init__(self, name, job):
        self.name = name
        self.job = job


    def display(self):
        print('name : {}, job : {}' .format(self.name, self.job))

p = parent('홍길동', '회사원')
p.display(

class children(parent):
    gender = None

    def __init__(self,name,job,gender):
        super().__init__(name, job)