"""
https://leetcode.com/problems/3sum/description/
Problem Statement:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Note that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""
from typing import List


def three_sum_to_zero(nums: List[int]) -> List[List[int]]:
    """
    Args:
        nums (List[int]): an array of integers
    Returns:
        List[List[int]]: an array of triplets [nums[i], nums[j], nums[k]] to zero by summation.
    Algo:
        use two pointers of low and high within a loop to find zero of summed items.
    Time:
        O(n^2)
    Space:
        O(1)
    """
    nums.sort()
    result = []
    for i in range(len(nums)):
        if nums[i] > 0: # to stop early from checking any more items in the loop. no need to check all positives because we are looking for summing items to zero.
            break
        if i == 0 or nums[i-1] != nums[i]: # skip the same items (duplicates)
            low, high = i + 1, len(nums) - 1
            while low < high:
                current_three_sum = nums[i] + nums[low] + nums[high]
                if current_three_sum == 0:
                    result.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low-1] == nums[low]:
                        low += 1
                elif current_three_sum < 0:
                    low += 1
                elif current_three_sum > 0:
                    high -= 1
    return result


if __name__ == "__main__":
    print(three_sum_to_zero([-1,0,1,2,-1,-4]))
    print(three_sum_to_zero([0, 1, 2, -1, -2, 4, -4]))
    print(three_sum_to_zero([0, 0,0,0,0,0]))
