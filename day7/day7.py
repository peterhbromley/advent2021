def read_input(filename):
    with open(filename) as f:
        return [int(x) for x in f.readline().strip().split(",")]


def find_median(nums):
    nums = sorted(nums)
    median_idx = len(nums) // 2
    if len(nums) % 2 == 0:
        return (nums[median_idx] + nums[median_idx - 1]) // 2
    else:
        return nums[median_idx]

nums = read_input("input.txt")
median = find_median(nums)
total_fuel = sum(abs(x - median) for x in nums)

print(f"Problem 1: {total_fuel}")


def calc_fuel(nums, pos):
    return sum(
        sum(i for i in range(1, abs(x - pos) + 1))
        for x in nums
    )


min_fuel = min(calc_fuel(nums, i) for i in range(min(nums), max(nums) + 1))

print(f"Problem 2: {min_fuel}")
