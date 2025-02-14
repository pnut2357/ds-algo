"""
Problem Statement
Given an array of characters where each char represents a fruit tree, you are given two baskets and your goal is to put max number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but once you have started you can't skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return max number of fruits in both baskets.
i.e.
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""

def fruits_in_baskets(fruits):
    import collections as colls
    fruit_dict = colls.defaultdict(int)
    start_window = 0
    max_length = 0
    for end_window in range(len(fruits)):
        fruit_dict[fruits[end_window]] += 1
        while len(fruit_dict) > 2:
            if fruit_dict[fruits[start_window]] == 1:
                del fruit_dict[fruits[start_window]]
            else:
                fruit_dict[fruits[start_window]] -= 1
            start_window += 1
        if len(fruit_dict) == 2:
            max_length = max(sum(fruit_dict.values()), max_length)
    return max_length

def sol_fruits_in_baskets(fruits):
    start_window = 0
    max_length = 0
    fruit_freq = {}
    for end_window in range(len(fruits)):
        right_pointer = fruits[end_window]
        if right_pointer not in fruit_freq:
            fruit_freq[right_pointer] = 0
        fruit_freq[right_pointer] += 1
        while len(fruit_freq) > 2:
            left_pointer = fruits[start_window]
            fruit_freq[left_pointer] -= 1
            if fruit_freq[left_pointer] == 0:
                del fruit_freq[left_pointer]
            start_window += 1
        max_length = max(sum(fruit_freq.values()), max_length)
    return max_length

if __name__ == "__main__":
    assert fruits_in_baskets(['A', 'B', 'C', 'A', 'C']) == 3, "incorrect"
    assert fruits_in_baskets(['A', 'B', 'C', 'B', 'B', 'C']) == 5, "incorrect"
    print(sol_fruits_in_baskets(['A', 'B', 'C', 'A', 'C']))
    print(sol_fruits_in_baskets(['A', 'B', 'C', 'B', 'B', 'C']))
