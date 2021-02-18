"""
 날짜 : 2021/02/18
 이름 : 이승환
 내용 : 교재 p46 - format과 양식문자 예
"""
# (4) format() 함수 인수 : format(value, "format")
print("원주율 =", format(3.14159, "8.3f"))
print("금액 =", format(10000, "10d"))
print("금액 =", format(125000, "3,d"))

# (5) 양식문자 인수 : print( "%양식문자" %(값) )
name = "홍길동"
age = 35
price = 125.456
print("이름 : %s, 나이 :%d, data = %.2f" %(name, age, price))