"""
날짜 : 2021/02/25
이름 : 이승환
내용 : 교재 p164 - 상속 예
"""
class super:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        def dsplay(self):
            print('name : %s, age : %d'%(self.name, self.age))

            sup =super
            sup.display()

class sub(super):
    gender = None

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print('name :%s, age : %d, gender : %s'%(self.name, self.age, self.gender))

sub = sub('자식', 25, '여자')
sub.display()