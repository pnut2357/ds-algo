"""
https://leetcode.com/problems/subarray-product-less-than-k/description/
Problem Statement
Given an array with positive numbers and a target number,
find all of its contiguous subarrays whose product is less than the target number.
i.e.
Example 1:
Input: [2, 5, 3, 10], target=30
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are 6 contiguous subarrays whose product is less than the target.

Example 2:
Input: [8, 2, 6, 5], target=50
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]
Explanation: There are 7 contiguous subarrays whose product is less than the target.
"""
def subarray_product_less_than_k(arr, target):
    """
    Args:
        arr (List[int]): an array of integers
        target (int): the target number
    Returns:
        number of the product of subarrays that is less than the target.
    Algo:
        Use two pointers to traverse the array and find the products less than k.
    [2, 5, 3, 10]
     ^
           ^
    """
    if target < 2:
        return 0
    left_ptr = 0
    counter = 0
    product = 1
    for right_ptr in range(len(arr)):
        product *= arr[right_ptr]
        while product >= target:
            product /= arr[left_ptr]
            left_ptr += 1
        counter += right_ptr - left_ptr + 1
    return counter

def sol_subarray_product_less_than_k(arr, target):
    import math
    if target == 0:
        return 0
    log_k = math.log(target, math.e)
    logs_prefix_sum = [0]
    for num in arr:
        logs_prefix_sum.append(logs_prefix_sum[-1] + math.log(num, math.e))
    counter = 0
    for i in range(len(logs_prefix_sum)):
        low = i+1
        high = len(logs_prefix_sum)
        while low < high:
            mid = (low + high)//2
            # the product of the subarray from i to mid is less than k
            if logs_prefix_sum[mid] - logs_prefix_sum[i] < log_k - 1e-9:
                low = mid + 1
            else:
                high = mid
        counter += low - 1 - i # all indices from i+1 to low-1
    return counter


if __name__ == '__main__':
    import math
    assert subarray_product_less_than_k([2, 5, 3, 10], 30), 6
    assert subarray_product_less_than_k([8, 2, 6, 5], 50), 7
    print(sol_subarray_product_less_than_k([2, 5, 3, 10], 30))
    print(sol_subarray_product_less_than_k([math.e, math.e**2, math.e**3, 10], 30))
    print(sol_subarray_product_less_than_k([8, 2, 6, 5], 50))



