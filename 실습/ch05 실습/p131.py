"""
날짜 : 2021/02/25
이름 : 이승환
내용 : 교재 p131 - 람다 함수 예
"""
# (1) 일반 함수
def Adder(x,y):
    add = x + y
    return add

print('add=', Adder(10, 20))

# (2) 림다 함수
print('add=', (lambda x,y: x + y)(10,20))