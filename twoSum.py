import time

def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        needed = target - nums[i]
        if needed in seen:
            return [seen[needed], i]
        seen[nums[i]] = i


def hash_Sum(nums, target):
    for i, x in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if x + nums[j] == target:
                return [i, j]


# SAME input size for fair comparison
input_data = list(range(50000))
target = 99999


# Brute-force timing
start = time.time()
hash_Sum(input_data, target)
stop = time.time()
print(f"Time Taken (Brute Force): {stop - start}")


# Hash-map timing
start = time.time()
twoSum(input_data, target)
stop = time.time()
print(f"Time Taken (Hash Map): {stop - start}")
