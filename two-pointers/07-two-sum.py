"""
https://leetcode.com/problems/two-sum/description/
Problem Statement:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
i.e.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

def two_sum(nums, target):
    hmap = {item: i for i, item in enumerate(nums)}
    for i in range(len(nums)):
        find_val = target - nums[i]
        if find_val in hmap and hmap[find_val] != i:
            return [i, hmap[find_val]]
    return []

if __name__ == "__main__":
    print(two_sum([2,7,11,15], 9))
    print(two_sum([3,2,4], 6))
