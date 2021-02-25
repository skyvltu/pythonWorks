"""
 날짜 : 2021/02/25
 이름 : 이승환
 내용 : 교재 p116 - builtins 함수와 import 함수 예
"""

# (1) builtins 함수
help(len)
dataset = list(range(1,6))
print(dataset)

print('len=', len(dataset))
print('sum=', sum(dataset)) # sum = 15
print('max=', max(dataset))
print('min=', min(dataset))

# (2) import 함수
import statistics # (방법1)
from statistics import variance, stdev # (방법2)

print('평균=', statistics.mean(dataset))
print('중위수=', statistics.median(dataset))
print("표본 분산=", variance(dataset))
print("표본 표준편차=", stdev(dataset))
