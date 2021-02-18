"""
 날짜 : 2021/02/18
 이름 : 이승환
 내용 : 교재 p47 - 외부상수 출력 예
"""
# (6) 외부 상수 인수
name = "홍길동"
age = 35
price = 125.456
print("이름 : {}, 나이 : {} , date={}".format(name,age,price))
print("이름 : {1}, 나이 : {0} , date={2}".format(age,name,price))

# (7) format 축약형(SQL문 작성)
uid = input("id input : ")
query = f"select * from member where uid = {uid}"
print(query)