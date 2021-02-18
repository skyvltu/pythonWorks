"""
 날짜 : 2021/02/18
 이름 : 이승환
 내용 : 교재 p36 - 파이썬 예약어 확인 예
"""

# 예약어 확인
import keyword #모듈 임포트

python_keyword = keyword.kwlist
print(python_keyword)
print( type(python_keyword) )
print( len(python_keyword) )