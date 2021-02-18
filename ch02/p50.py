"""
 날짜 : 2021/02/18
 이름 : 이승환
 내용 : 교재 p50 - 슬라이싱 예
"""
# (1) 왼쪽 기준
oneLine = 'this is one line string'
print(oneLine)
print("문자열 길이 :", len(oneLine))
print(oneLine[0 : 4])
print(oneLine[:4])
print(oneLine[:])
print(oneLine[::2])

# (2) 오른쪽 기준
print(oneLine[0:-1:2])
print((oneLine[-6:-1]))
print(oneLine[-6:])

# (3) 부분 문자열 생성
substring = oneLine[-11: ]
print(substring)