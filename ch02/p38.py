"""
 날짜 : 2021/02/18
 이름 : 이승환
 내용 : 교재 p38 - 자료형 변환 예
"""
# 실수 -> 정수
a = int(10.5)
b = int(20.42)
add = a + b
print('add = ', add)

# 정수 -> 실수
a = float(10)
b = float(20)
add2 = a + b
print('add2 = ', add2)

# 논리형 -> 정수
print( int(True) ) # 1
print( int(False) ) # 0

# 문자형 -> 정수
st = '10'
print( int(st) ** 2 ) # 제곱 연산