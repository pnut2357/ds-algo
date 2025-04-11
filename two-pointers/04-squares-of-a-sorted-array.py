"""
https://leetcode.com/problems/squares-of-a-sorted-array/description/
977. Squares of a Sorted Array
Problem Statement:
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number, also in non-decreasing order.
i.e.
Input: nums = [-2, -1, 0, 2, 3]
               2   1   0  2  3
Output: [0, 1, 4, 4, 9]

Input: nums = [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]

Input: nums = [-7, -3, 2, 3, 11, 12]
Output: [4, 9, 9, 49, 121, 144]
"""
def sorted_squares(nums):
    """
    O(n*logn)
    O(n)
    """
    return sorted(i**2 for i in nums)


def sol_sorted_squares(nums):
    n = len(nums)
    result = [0]*n
    left = 0
    right = n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        result[i] = square**2
    return result


if __name__ == "__main__":
    assert sorted_squares([-2, -1, 0, 2, 3]) == [0, 1, 4, 4, 9]
    print(sorted_squares([-2, -1, 0, 2, 3]))