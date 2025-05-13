import sys


def median(nums):
    sorted_nums = sorted(nums)
    n = len(sorted_nums)

    if n % 2 == 1:
        return sorted_nums[n // 2]
    else:
        return (sorted_nums[n // 2] + sorted_nums[n // 2 - 1]) // 2


def counts(mid, nums):
    return sum(abs(num - mid) for num in nums)


def main():
    """
    Команда для запуска
    python3 task4.py nums.txt

    """
    file = sys.argv[1]
    with open(file, 'r') as f:
        lines = f.readlines()
        nums = list(map(int, lines))
    mid = median(nums)
    result = counts(mid, nums)
    print(result)


main()
