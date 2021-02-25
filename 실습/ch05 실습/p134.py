"""
날짜 : 2021/02/25
이름 : 이승환
내용 : 교재 p134 - 일급함수와 함수 클로저 예
"""

def a():
    print('a 함수')
    def b():
        print('b 함수')
    return b
b = a()
b()

data = list(range(1, 101))
def outer_func(data):
    dataset = data
    def tot():
        tot_val = sum(dataset)
        return tot_val
    def avg(tot_val):
        avg_val = tot_val / len(dataset)
        return avg_val
    return tot, avg

tot, avg = outer_func(data)

tot_val =tot()
print('tot =', tot_val)
avg_val = avg(tot_val)
print('avg =', avg_val)