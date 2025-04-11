"""
Problem Statement:
Given an array containing 0s and 1s, if you are allowed to replace no more than 'k' 0s and 1s, find the length of the longest contiguous subarray having all 1s.
i.e.
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
                             _        _
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
"""

def length_of_longest_substring(arr, k):
    """
    Args:
        arr: array of integers
        k: number of replacing zeros
    Returns:
        longest contiguous subarray having all 1s
    Algo:
        [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
                        ^
                                       ^
        one_counter = 4
        right_ptr - left_ptr + 1 - one_counter = 6-4 = 2
        max_length = 6
    O(n)
    O(1)
    """
    left_ptr = 0
    one_counter = 0
    max_length = 0
    for right_ptr in range(len(arr)):
        if arr[right_ptr] == 1:
            one_counter += 1
        while right_ptr - left_ptr + 1 - one_counter > k: # number of zeros in the window; if zeros exceed k, shrink window.
            if arr[left_ptr] == 1:
                one_counter -= 1
            left_ptr += 1
        max_length = max(right_ptr-left_ptr+1, one_counter)
    return max_length

def sol_longest_substring(arr, k):
    left_ptr = 0
    num_ones = 0
    for right_ptr in range(len(arr)):
        if arr[right_ptr] == 1:
            num_ones += 1
        while right_ptr - left_ptr + 1 - num_ones > k:
            if arr[left_ptr] == 1:
                num_ones -= 1
            left_ptr += 1
        max_length = max(right_ptr-left_ptr+1, num_ones)
    return max_length



if __name__ == '__main__':
    assert length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2) == 6, "incorrect"
    assert length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3) == 9, "incorrect"
    print(sol_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(sol_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
