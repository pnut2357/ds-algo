"""
https://leetcode.com/problems/3sum-closest/description/
Problem Statement:
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target as possible.
i.e.
Example 1:
Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

Example 2:
Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

Example 3:
Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
"""
import math
def three_sum_close_to_target(arr, target):
    arr.sort()
    closest_sum = math.inf
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        low, high = i+1, len(arr) - 1
        while low < high:
            three_sum = arr[i] + arr[low] + arr[high]
            # closest_sum = min(abs(three_sum - target), closest_sum)
            if abs(three_sum - target) < abs(closest_sum - target):
                closest_sum = three_sum
            if three_sum == target:
                return three_sum
            elif three_sum < target:
                low += 1
            elif three_sum > target:
                high -= 1
    return closest_sum

if __name__ == '__main__':
    print(three_sum_close_to_target([-2, 0, 1, 2], 2))

