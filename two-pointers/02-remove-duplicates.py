"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/editorial/
26. Remove Duplicates from Sorted Array
Problem Statement:
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.
i.e.
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Input: [2, 2, 2, 11]
    l            ^
    r            ^
    dups = 3
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
"""
def remove_duplicates(arr):
    removed_array_length = len(arr)
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            removed_array_length -= 1
    return removed_array_length

def sol_remove_duplicates(arr):
    """
    Args:
        arr (List[int]): an array of integers
    Returns:
        length of the array after removing the duplicates
    Algo:
        use two adjacent pointers i-1, i to swap the i-th element and the earliest duplicate (insert_index).
    [2, 3, 3, 3, 6, 9, 9]
    [2, 3, 6, 9, 6, 9, 9]
                    ^  ^
                in
    insert_index = 4
    """
    insert_index = 1
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            arr[insert_index] = arr[i]
            insert_index += 1
    return insert_index

if __name__ == "__main__":
    assert remove_duplicates([2, 3, 3, 3, 6, 9, 9]) == 4
    assert remove_duplicates([2, 2, 2, 11]) == 2
    print(sol_remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(sol_remove_duplicates([2, 2, 2, 11]))