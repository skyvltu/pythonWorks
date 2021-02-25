"""
날짜 : 2021/02/25
이름 : 이승환
내용 : 교재 p142 - 1~n 정수 누적합 예
"""
def Adder(n):
    if n == 1:
        return 1
    else:
        result = n + Adder(n-1)

        print(n, end = ' ')
        return result

print('n=1 :', Adder(1))
print('\nn=5 :', Adder(5))