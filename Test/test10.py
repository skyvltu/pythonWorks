"""
날짜 : 2021/03/11
이름 : 이승환
내용 : 파이썬 연습문제 10. 예외처리
"""
import math, random

answer = math.ceil(random.random() * 45)
number = 0
count = 0

while True:
    count += 1
    print('------------------------')
    print('answer를 맞춰보세요.')
    number = input('1 ~ 45 사이의 값 입력 : ')

    try:
        number = int(number)
    except:
        print('숫자를 입력하십시요!')
        continue

    if number < 0:
        print('음수를 입력 할 수 없습니다.')
        continue

    if answer > number:
        print('더 큰 수를 입력하세요.')

    elif answer < number:
        print('더 작은 수를 입력하세요.')

    else:
        print('정답 :', answer)
        print('맞추셨습니다!')
        print('시도횟수 : %d회' % count)
        break

print('프로그램 정상종료...')