"""
날짜 : 2021/02/25
이름 : 이승환
내용 : 교재 p129 - 가변인수를 갖는 함수 예
"""
# (1) 튜플형 가변인수
def Func1 (name, *names):
    print(name) # 실인수 : 홍길동
    print(names) # 실인수 : ('이순신', '유관순')

Func1("홍길동","이순신","유관순")

# (2) 통계량 구하는 함수
def statis(func, *data):
    if func == 'avg':
        return mean(data)
    elif func == 'var':
        return variance(data)
    elif func == 'std':
        return stdev(data)
    else:
        return 'TypeError'

# statis 함수 호출
print('avg=', statis('avg', 1, 2, 3, 4, 5))
print('var=', statis('var', 1, 2, 3, 4, 5))
print('std=', statis('std', 1, 2, 3, 4, 5))

# (3) 딕트형 가변인수
def emp_func(name, age, **other):
    print(name)
    print(age)
    print(other)

# emp_func 함수 호출
emp_func('홍길동','35',addr='서울시', height=175, weight=65)

