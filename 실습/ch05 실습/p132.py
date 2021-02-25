"""
날짜 : 2021/02/25
이름 : 이승환
내용 : 교재 p132 - 함수 스코프 예
"""
# (1) 지역변수 예
x = 50 # 전역변수
def local_func(x):
    x += 50 #지역변수 -> 종료 소멸 시점
local_func(x)
print('x=', x)

# (2) 전역변수 예
def global_func():
    global x #전역변수 x 사용
    x += 50
global_func()
print('x=', x)