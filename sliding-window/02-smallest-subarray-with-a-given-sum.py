"""
Problem Statement
Given an array of (+) nums and a (+) num 'S', find the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'. Return 0 if no such subarray exists.
e.g.
Input: [2,1,5,2,3,2], S=7
Output: 2
Explanation: The smallest subarray with a sum >= 7 is [5,2]

Input: [2,1,5,2,8], S=7
Output: 1
Explanation: The smallest subarray with a sum >= 7 is [8]

Input: [3,4,1,1,6], S=8
Output: 3
Explanation: The smallest subarray with a sum >= 8 is [3,4,1]
"""


def smallest_subarray_with_given_sum(arr, s):
    """
    Args:
        arr (List[int]): an array of positive integers.
        s (int): the threshold number that must be greater than or equal to sum of smallest subarray.
    Returns:
        length of subarray with sum <= s.
    Algo:
        use sliding window to
    [2,1,5,2,3,2], S=7
     ^ ^
    Complexity:
        Time: O(n)
        Space: O(1)
    """
    start_window = 0
    sum_window = 0
    length_subarray = len(arr)
    for end_window in range(length_subarray):
        sum_window += arr[end_window]
        while sum_window >= s:
            length_subarray = min(length_subarray, end_window-start_window+1)
            sum_window -= arr[start_window]
            start_window += 1
    return length_subarray


def sol_smallest_subarray_with_given_sum(arr, s):
    import math
    window_sum = 0
    min_length = math.inf
    window_start = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_length == math.inf:
        return 0
    return min_length


if __name__ == '__main__':
    assert smallest_subarray_with_given_sum([2,1,5,2,3,2], 7) == 2, "incorrect"
    assert smallest_subarray_with_given_sum([2,1,5,2,8], 8) == 1, "incorrect"
    assert smallest_subarray_with_given_sum([3,4,1,1,6], 8) == 3, "incorrect"
    print(sol_smallest_subarray_with_given_sum([2,1,5,2,3,2], 7))
    print(sol_smallest_subarray_with_given_sum([2,1,5,2,8], 8))
    print(sol_smallest_subarray_with_given_sum([3,4,1,1,6], 8))