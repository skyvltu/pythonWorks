"""
날짜 : 2021/03/11
이름 : 이승환
내용 : 파이썬 연습문제 4. 리스트
"""
numbers = [17, 92, 18, 33, 58, 7, 26, 42]
maxNum = numbers[0]

for num in numbers:

    if maxNum < num:
        maxNum = num

print('numbers에서 가장 큰 수 :', maxNum)