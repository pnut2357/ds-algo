"""
Problem Statement
Given an array of positive numbers and a positive number 'k', find the max sum of any contiguous sub-array of size 'k'.
e.g.
Input: [2,1,5,1,3,2], k=3
Output: 9
Explanation: SUbarray with max sum is [5,1,3]

Input: [2,3,4,1,5], k=2
Output: 7
Explanation: SUbarray with max sum is [3,4]
"""

def max_subarray_of_size_k(arr, k):
    """
    Args:
        arr: array of postive nums
        k: size of subarray
    Returns:
        the max sum of subarray.
    Algo:
        max_val = 0
        Use a for-loop to extract the window sum and compare the max val.
    [2,1,5,1,3,2]
           ^   ^
    window_sum = 6
    max_val = 9
    max_val = max(window_sum, max_val)
    Complexity:
        Time: O(n)
        Space O(1)
    """
    max_val = 0
    for i in range(len(arr)-k+1):
        window_sum = sum(arr[i:i+k])
        max_val = max(window_sum, max_val)
    return max_val

def sol_max_subarray_of_size_k2(arr, k):
    max_sum = 0
    window_sum = 0
    window_start = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k-1:
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum

if __name__ == "__main__":
    assert max_subarray_of_size_k([2, 1, 5, 1, 3, 2], 3) == 9, "incorrect"
    assert max_subarray_of_size_k([2, 3, 4, 1, 5], 2) == 7, "incorrect"
    print(sol_max_subarray_of_size_k2([2, 1, 5, 1, 3, 2], 3))
    print(sol_max_subarray_of_size_k2([2, 3, 4, 1, 5], 2))
