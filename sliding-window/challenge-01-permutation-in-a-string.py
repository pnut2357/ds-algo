"""
Problem Statement:
Given a string and a pattern, find out if the string contains any permutation of the pattern.
i.e.
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
"""

def find_permutation(string, pattern):
    """
    for _ in aaacb
    a: 3
    b: 1
    c: 1
    abc
    """
    import collections as colls
    string_set = colls.defaultdict(int)
    for item in string:
        string_set[item] += 1
    for ch in pattern:
        if ch in string_set:
            string_set[ch] -= 1
    if min(string_set.values()) >= 0:
        return True
    elif min(string_set.values()) < 0:
        return False

def sol_find_permutation(string, pattern):
    import collections as colls
    left_ptr = 0
    matched_counter = 0
    char_counter = colls.defaultdict(int)
    for ch in pattern:
        char_counter[ch] += 1
    for right_ptr in range(len(string)):
        right_ch = string[right_ptr]
        if right_ch in char_counter:
            char_counter[right_ch] -= 1
            if char_counter[right_ch] == 0:
                matched_counter += 1
        if matched_counter == len(char_counter):
            return True
        if right_ptr >= len(string) - 1:
            left_ch = string[left_ptr]
            left_ptr += 1
            if left_ch in char_counter:
                if char_counter[left_ch] == 0:
                    matched_counter -= 1
                char_counter[left_ch] -= 1
    return False

if __name__ == "__main__":
    assert find_permutation("oidbcaf", "abc") == True, "incorrect"
    assert find_permutation("odicf", "dc") == True, "incorrect"
    assert find_permutation("bcdxabcdy", "bcdyabcdx") == True
    # assert find_permutation("eidboaoo", "ab") == False
    print(sol_find_permutation("oidbcaf", "abc"))
    print(sol_find_permutation("odicf", "dc"))
    print(sol_find_permutation("bcdxabcdy", "bcdyabcdx"))
    print(sol_find_permutation("aaacb", "abc"))
    print(sol_find_permutation("eidboaoo", "ab"))
