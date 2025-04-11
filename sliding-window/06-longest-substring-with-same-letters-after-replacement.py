"""
https://leetcode.com/problems/longest-repeating-character-replacement/description/
Problem Statement:
Given a string with lowercase letters only, if you are allowed to replace no more than 'k' letters with any letter, find the length of the longest substring having the same letters after replacement.
i.g.
Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb"

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb"

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'd' or 'b' with 'c' to have a longest repeating substring "ccc"

  aabccbb
      ^
  ^
  mydict = {a: 2, b: 1, c: 2}
  while len(mydict) > k:
    del key in mydict or subtract value in mydict
    left_ptr ++
    max_length = max(max_length, right_ptr - left_ptr + 1)
"""
def length_of_longest_substring(string, k):
    left_ptr = 0
    letter_counter = {}
    max_length = 0
    for right_ptr in range(len(string)):
        if string[right_ptr] not in letter_counter:
            letter_counter[string[right_ptr]] = 1
        else:
            letter_counter[string[right_ptr]] += 1
        longest_count = max(letter_counter.values())
        # subtring_size = right_ptr - left_ptr + 1
        # You must not use subtring_size because left_ptr keeps updated during while loop.
        while right_ptr - left_ptr + 1 - longest_count > k:
            if letter_counter[string[left_ptr]] == 0:
                del letter_counter[string[left_ptr]]
            letter_counter[string[left_ptr]] -= 1
            left_ptr += 1
        max_length = max(max_length, right_ptr - left_ptr + 1)
    return max_length

def sol_length_of_longest_substring(string, k):
    import collections as colls
    window_start = 0
    max_length = 0
    letter_counter = colls.defaultdict(int)
    for window_end in range(len(string)):
        right_char = string[window_end]
        letter_counter[right_char] += 1
        longest_count = max(letter_counter.values())
        while window_end - window_start + 1 - longest_count > k:
            left_char = string[window_start]
            letter_counter[left_char] -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length

if __name__ == '__main__':
    assert length_of_longest_substring("aabccbb", 2) == 5
    assert length_of_longest_substring("abbcb", 1) == 4
    assert length_of_longest_substring("abccde", 1) == 3
    print(sol_length_of_longest_substring("aabccbb", 2))
    print(sol_length_of_longest_substring("abbcb", 1))
    print(sol_length_of_longest_substring("abccde", 1))



