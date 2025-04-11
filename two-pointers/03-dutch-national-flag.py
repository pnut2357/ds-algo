"""
Problem Statement:
Given an array containing 0s, 1s, and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can't count 0s, 1s, and 2s to recreate the array.
i.e.
Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]

Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]
"""

def sort_dutch_flag(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else: # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr
if __name__ == "__main__":
    assert sort_dutch_flag([0, 1, 2, 1, 0]) == [0, 0, 1, 1, 2]
    assert sort_dutch_flag([2, 2, 0, 1, 2, 0]) == [0, 0, 1, 2, 2, 2]