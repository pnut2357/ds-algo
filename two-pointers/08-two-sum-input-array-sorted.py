"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Problem Statement:
Given an array of integers nums that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
i.e.
Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""

def two_sum_sorted_input_array(nums, target):
    left_ptr = 0
    right_ptr = len(nums) - 1
    while left_ptr < right_ptr:
        if nums[left_ptr] + nums[right_ptr] == target:
            return [left_ptr+1, right_ptr+1]
        elif nums[left_ptr] + nums[right_ptr] > target:
            right_ptr -= 1
        else:
            left_ptr += 1
    return []

if __name__ == "__main__":
    print(two_sum_sorted_input_array([2,7,11,15], 9))
    print(two_sum_sorted_input_array([2,3,4], 6))
