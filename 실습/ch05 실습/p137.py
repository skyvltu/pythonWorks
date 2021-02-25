"""
날짜 : 2021/02/25
이름 : 이승환
내용 : 교재 p137 - 획득자와 지정자 예
"""
def main_func(num):
    num_val = num
    def getter():
        return num_val
    def setter(value):
        nonlocal num_val
        num_val = value

    return getter, setter

getter, setter = main_func(100)

print('num =', getter())

setter(200)
print('num', getter())