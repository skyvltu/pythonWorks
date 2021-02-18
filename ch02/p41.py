"""
 날짜 : 2021/02/18
 이름 : 이승환
 내용 : 교재 p41 - 대입연산자 예
"""
# (1) 변수에 값 할당 (=)
i = tot = 10 # i=10; tot =10
i += 1 # i = i + 1
tot += i # tot = tot + i
print(i, tot)

# 같은 줄에 중복 출력
print('출력1', end=' , ') # end='구분자'
print('출렬2')

v1, v2 = 100, 200

# (2) 변수 교체
v2, v1 = v1, v2
print(v1, v2) # 200 100

# (3) 패킹(packing) 할당
1st = [1, 2, 3, 4, 5]
v1, *v2 = 1st
print(v1,v2)

*v1, v2 = 1st
print(v1, v2)