"""
날짜 : 2021/02/25
이름 : 이승환
내용 : 교재 p140 - 숫자 카운트 예
"""
def counter(n):
    if n == 0:
        return 0
    else:
        counter(n-1)

print('n=0 :', counter(0))

counter(5)