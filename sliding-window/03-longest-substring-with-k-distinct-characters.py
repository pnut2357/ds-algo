"""
Problem Statement:
Given a string, find the length of the longest substring in the string with no more than K distinct characters.
e.g.
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than 2 distinct characters is "araa".

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than 1 distinct characters is "aa".

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substring with no more than 3 distinct characters is "cbbeb" and "bbebi".
"""

def longest_substring_with_k_distinct(str_arr, k):
    """
    Args:
        str: String
        k: int
    Returns:
        the longest substring with no more than k distinct characters.
    Algo:
        use two pointers in a for-loop to find the length of the distinct char.
        araaci, k=2
         ^
            ^
        {a: 2, r: 1, c: 1}
    """
    import collections as coll
    char_dict = coll.defaultdict(int)
    start_window = 0
    max_length = 0
    for end_window in range(len(str_arr)):
        char_dict[str_arr[end_window]] += 1

        while len(char_dict) > k:
            if char_dict[str_arr[start_window]] == 1:
                del char_dict[str_arr[start_window]]
            elif char_dict[str_arr[start_window]] > 1:
                char_dict[str_arr[start_window]] -= 1
            start_window += 1
        if len(char_dict) == k:
            max_length = max(sum(char_dict.values()), max_length)
    return max_length

def sol_longest_substring_with_k_distinct(str_arr, k):
    window_start = 0
    max_length = 0
    char_dict = {}
    for window_end in range(len(str_arr)):
        right_pointer = str_arr[window_end]
        if right_pointer not in char_dict:
            char_dict[right_pointer] = 0
        char_dict[right_pointer] += 1
        while len(char_dict) > k:
            left_pointer = str_arr[window_start]
            char_dict[left_pointer] -= 1
            if char_dict[left_pointer] == 0:
                del char_dict[left_pointer]
            window_start += 1
        max_length = max(max_length, sum(char_dict.values()))
    return max_length


if __name__ == '__main__':
    assert longest_substring_with_k_distinct("araaci", 2) == 4, "incorrect"
    assert longest_substring_with_k_distinct("araaci", 1) == 2, "incorrect"
    assert longest_substring_with_k_distinct("cbbebi", 3) == 5, "incorrect"
    print(sol_longest_substring_with_k_distinct("araaci", 2))
    print(sol_longest_substring_with_k_distinct("araaci", 1))
    print(sol_longest_substring_with_k_distinct("cbbebi", 3))