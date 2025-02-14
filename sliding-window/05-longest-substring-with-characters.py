"""
Problem Statement
Given a string, find the length of the longest substring which has no repeating characters.
i.e.
Input: String="aabccbb"
  right_char   ^
  start_window 0 >> 1 >>
  string_right_char_idx {a: 0}

Step	right_char	start_window	string_right_char_idx	end_window	max_length
1	'a'	0	            {'a': 0}	0	1
2	'a'	1 (duplicate)	{'a': 1}	1	1
3	'b'	1	            {'a': 1, 'b': 2}	2	2
4	'c'	1	            {'a': 1, 'b': 2, 'c': 3}	3	3
5	'c'	4 (duplicate)	{'a': 1, 'b': 2, 'c': 4}	4	3
6	'b'	4 (duplicate)	{'a': 1, 'b': 5, 'c': 4}	5	3
7	'b'	6 (duplicate)	{'a': 1, 'b': 6, 'c': 4}	6

Output: 3
Explanation: The longest substring without any repeating characters is "abc"

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab"

Input: String="abccde"
Output: 3
Explanation: The longest substring without any repeating characters is "abc" & "cde"


"""
def non_repeat_substring(string):
    import collections as colls
    string_right_char_idx = colls.defaultdict(int)
    start_window = 0
    max_length = 0
    for end_window in range(len(string)):
        right_char = string[end_window]
        if right_char in string_right_char_idx:
            start_window = max(start_window, string_right_char_idx[right_char]+1)
        string_right_char_idx[right_char] = end_window
        max_length = max(max_length, end_window - start_window + 1)
    return max_length

def sol_non_repeat_substring(string):
    start_window = 0
    max_length = 0
    char_index_dict = {}
    for end_window in range(len(string)):
        right_char = string[end_window]
        if right_char in char_index_dict:
            start_window = max(start_window, char_index_dict[right_char]+1)
        char_index_dict[right_char] = end_window
        max_length = max(max_length, end_window-start_window+1)
    return max_length

if __name__ == '__main__':
    assert non_repeat_substring("aabccbb") == 3, "incorrect"
    assert non_repeat_substring("abbbb") == 2, "incorrect"
    assert non_repeat_substring("abccde") == 3, "incorrect"
    print(sol_non_repeat_substring("aabccbb"))
    print(sol_non_repeat_substring("abbbb"))
    print(sol_non_repeat_substring("abccde"))

