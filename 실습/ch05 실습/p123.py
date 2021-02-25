"""
 날짜 : 2021/02/25
 이름 : 이승환
 내용 : 교재 p123 - 사용자 정의함수 예
"""

# (1) 인수가 없는 함수
def userFunc1 () :
    print('인수가 없는 함수')
    print('userFunc1')

userFunc1()

# (2) 인수가 있는 함수
def userFunc2 (x,y) :
    print('userFunc2')
    z = x + y
    print('z=', z)

userFunc2(10,20) #함수 호출

# (3) return 있는 함수
def userFunc3 (x,y) :
    print('userFunc3')
    tot = x + y
    sub = x - y
    mul = x * y
    div = x / y

    return tot, sub, mul, div

# 실인수 : 키보드 입력
x = int(input('x입력 : '))
y = int(input('y입력 : '))

t, s, m, d = userFunc3(x,y)
print('tot =', t)
print('sub =', s)
print('mul =', m)
print('div =', d)