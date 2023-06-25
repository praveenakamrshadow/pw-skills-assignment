import random


def moveZeroes(nums):
    zero_count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i - zero_count] = nums[i]
            if zero_count > 0:
                nums[i] = 0
        else:
            zero_count += 1
    return nums + [0] * zero_count


def generate_random_array(size):
    nums = [random.randint(-10, 10) for _ in range(size)]
    return nums


def print_array(arr):
    print("[", end="")
    for i in range(len(arr)):
        if i != len(arr) - 1:
            print(arr[i], end=", ")
        else:
            print(arr[i], end="")
    print("]")


array_size = random.randint(5, 10)
nums = generate_random_array(array_size)

print("Original array:")
print_array(nums)

result = moveZeroes(nums)

print("\nArray after moving zeroes to the end:")
print_array(result)
