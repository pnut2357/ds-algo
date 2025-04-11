"""
1. Two Sum
https://leetcode.com/problems/two-sum/description/
Problem Statement:
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
i.e.
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

  1 2 3 4 6
  ^
  ^
"""

def pair_with_target_sum(arr, target):
    """
    O(n)
    O(n)
    """
    import collections as colls
    nums_idx = colls.defaultdict(int)
    for i in range(len(arr)):
        nums_idx[arr[i]] += i
    for i in range(len(arr)):
        x = target - arr[i]
        if x in nums_idx and i != nums_idx[x]:
            return [i, nums_idx[x]]
    return []
def sol_pair_with_target_sum(arr, target):
    import collections as colls
    nums_index = colls.defaultdict(int)
    for idx in range(len(arr)):
        nums_index[arr[idx]] = idx
        complement = target - arr[idx]
        if complement in nums_index and idx != nums_index[complement]:
            return [idx, nums_index[complement]]
    return []

if __name__ == "__main__":
    assert pair_with_target_sum([1, 2, 3, 4, 6], 6) == [1, 3]
    assert pair_with_target_sum([2, 5, 9, 11], 11) == [0, 2]
    print(sol_pair_with_target_sum([1, 2, 3, 4, 6], 6))
    print(sol_pair_with_target_sum([2, 5, 9, 11], 11))

