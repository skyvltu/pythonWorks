"""
날짜 : 2021/03/11
이름 : 이승환
내용 : 파이썬 연습문제 5. 리스트 선택정렬
"""

nums = [4, 2, 1, 5, 3]

for i in range(4):

    for j in range(i+1, 5):

        if nums[i] > nums[j]:

            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp

# 정렬 후 출력
for n in nums:
    print(n, end=', ')
