import sys

n = int(sys.argv[1])
m = int(sys.argv[2]) - 1

nums = [i for i in range(1, n + 1)]
nums1 = []
start = 0
check = set()
"""
Можно еще было сделать через срезы в Python, но так нагляднее

Команда для запуска
python3 task1.py 5 4

"""
while start not in check:
    check.add(start)
    nums1.append(nums[start])
    start = (start + m) % n
print(''.join(map(str, nums1)))