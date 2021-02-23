from ch06.lib.student import student

class Salarystudent(student):

    __company = None

    def __init__(self, name, age, school, major, company):
        super().__init__(name, age, school, major)
        self.__company = company

    def hello(self):
        super().hello()
        print('회사 :', self.__company)