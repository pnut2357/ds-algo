"""
https://leetcode.com/problems/3sum-smaller/
Problem Statement:
Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
i.e.
Example 1:
Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]

Example 2:
Input: nums = [], target = 0
Output: 0

Example 3:
Input: nums = [0], target = 0
Output: 0
"""
def three_sum_smaller(nums, target):
    """
    Args:
        nums (List[int]): an array of integers
        target (int): an integer to be found
    Returns:
        number of summed triplets satisfying less than target.
    Algo:
        1. Sort the array - O(n log n)
        2. Use three pointers: i, low, and high
        3. For each i, find all pairs (low, high) where sum < target
        4. When sum < target, count all numbers between low and high
    Time Complexity: O(n^3)
    Space Complexity: O(1) if we don't count the space for sorting
    """
    nums.sort()
    result = []
    for i in range(len(nums)):
        low, high = i + 1, len(nums) - 1
        while low < high:
            current_three_sum = nums[i] + nums[low] + nums[high]
            if current_three_sum < target:
                for k in range(low + 1, high + 1):
                    result.append([nums[i], nums[low], nums[k]])
                low += 1
            else:
                high -= 1
    
    return len(result)

def sol_three_sum_smaller(nums, target):
    """
    Args:
        nums (List[int]): an array of integers
        target (int): an integer to be found
    Returns:
        number of summed triplets satisfying less than target.
    Algo:
        1. Sort the array - O(n log n)
        2. Use three pointers: i, low, and high
        3. For each i, find all pairs (low, high) where sum < target
        4. When sum < target, count all numbers between low and high
    """
    if len(nums) < 3:
        return 0
    count = 0
    nums.sort()
    for i in range(len(nums)):
        low, high = i + 1, len(nums) - 1
        while low < high:
            current_three_sum = nums[i] + nums[low] + nums[high]
            if current_three_sum < target:
                # Count all valid triplets between low and high
                count += high - low
                low += 1
            else:
                high -= 1
    return count

    

if __name__ == "__main__":
    print(three_sum_smaller([-2,0,1,3], 2))  # Should print 2
    print(sol_three_sum_smaller([-2,0,1,3], 2))  # Should print 2
