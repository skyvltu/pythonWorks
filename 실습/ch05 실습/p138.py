"""
날짜 : 2021/02/25
이름 : 이승환
내용 : 교재 p138 - 함수 장식자 예
"""
def wrap(func):
    def decorated():
        print('방가워요!')
        func()
        print('잘가요!')
    return  decorated

@wrap
def hello():
    print('hi ~', "홍길동")

hello()