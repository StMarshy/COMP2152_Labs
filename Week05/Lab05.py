# Week 05 Lab: Recursion & Functions - Starter Code
# COMP2152 - Python Programming

print("=" * 60)
print("WEEK 05 LAB: RECURSION & FUNCTIONS")
print("=" * 60)

# ============================================================
# Question 1: Fibonacci Number (LeetCode #509)
# ============================================================
print("\n" + "=" * 50)
print("Question 1: Fibonacci Number (#509)")
print("=" * 50)


def fib(n):

    # Base case 1
    if n == 0:
        return 0

    # Base case 2
    if n == 1:
        return 1

    # Recursive case
    return fib(n - 1) + fib(n - 2)


print("Fibonacci Sequence (F(0) to F(10)):")
print("-" * 30)
for i in range(11):
    result = fib(i)
    print("F(" + str(i) + ") = " + str(result))

print("\nAdditional test cases:")
print("F(15) = " + str(fib(15)))
print("F(20) = " + str(fib(20)))


# ============================================================
# Question 2: FizzBuzz (LeetCode #412)
# ============================================================
print("\n" + "=" * 50)
print("Question 2: FizzBuzz (#412)")
print("=" * 50)


def fizz_buzz(n):

    result = []

    for i in range(1, n + 1):

        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")

        elif i % 3 == 0:
            result.append("Fizz")

        elif i % 5 == 0:
            result.append("Buzz")

        else:
            result.append(str(i))

    return result


print("\nTest Case 1: n = 3")
print("Output:", fizz_buzz(3))

print("\nTest Case 2: n = 5")
print("Output:", fizz_buzz(5))

print("\nTest Case 3: n = 15")
print("Output:", fizz_buzz(15))

print("\nTest Case 4: n = 1")
print("Output:", fizz_buzz(1))


# ============================================================
# Question 3: Binary Search (LeetCode #704)
# ============================================================
print("\n" + "=" * 50)
print("Question 3: Binary Search (#704)")
print("=" * 50)


# Part A: Iterative
def binary_search_iterative(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif target < nums[mid]:
            right = mid - 1

        else:
            left = mid + 1

    return -1


# Part B: Recursive
def binary_search_recursive(nums, target, left, right):

    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    if target < nums[mid]:
        return binary_search_recursive(nums, target, left, mid - 1)

    return binary_search_recursive(nums, target, mid + 1, right)


def search_recursive(nums, target):
    return binary_search_recursive(nums, target, 0, len(nums) - 1)


# Tests
print("\n--- Iterative Binary Search ---")
test_cases = [
    ([-1, 0, 3, 5, 9, 12], 9),
    ([-1, 0, 3, 5, 9, 12], 2),
    ([1], 1),
    ([1, 2, 3, 4, 5], 1),
    ([1, 2, 3, 4, 5], 5),
    ([1, 2, 3, 4, 5], 3),
    ([], 5),
]

for nums, target in test_cases:
    print(nums, target, "->", binary_search_iterative(nums, target))

print("\n--- Recursive Binary Search ---")
for nums, target in test_cases:
    print(nums, target, "->", search_recursive(nums, target))


# ============================================================
# Summary (commented so Python doesn't treat as code)
# ============================================================

# Key Concepts to Practice:
# 1. Fibonacci — recursion with base cases
# 2. FizzBuzz — correct order of conditions
# 3. Binary Search — divide and conquer O(log n)
# Array MUST be sorted!
