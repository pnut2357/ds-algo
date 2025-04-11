"""
https://leetcode.com/problems/happy-number/description/
Problem Statement
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

i.e.
Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false
"""

def is_happy_number(n: int) -> bool:
    """
    Args:
        n: int
    Returns:
        bool
    Algo:
        Use Floyd's Cycle Detection (tortoise and hare) to detect cycles.
        - If we reach 1, it's a happy number
        - If we detect a cycle that doesn't include 1, it's not a happy number
    """
    slow = n
    fast = n
    while True:
        slow = sum_of_squares(slow)  # Move one step
        fast = sum_of_squares(sum_of_squares(fast))  # Move two steps
        
        if fast == 1:  # Found 1, it's a happy number
            return True
        if slow == fast:  # Detected a cycle that's not 1
            return False

def sum_of_squares(n: int) -> int:
    """Calculate the sum of squares of digits in a number."""
    result = 0
    while n > 0:
        digit = n % 10
        result += digit ** 2
        n //= 10
    return result

def sol_is_happy_number(n: int) -> bool:
    """
    Args:
        n: int
    Returns:
        bool
    """
    visit = set()
    while n != 1 and n not in visit:
        visit.add(n)
        n = sum_of_squares(n)
        if n == 1:
            return True
    return False


if __name__ == "__main__":
    print(is_happy_number(19))  # Should print True
    print(is_happy_number(2))   # Should print False
    print(is_happy_number(139)) # 
    print(is_happy_number(1679))
    print("--------------------------------")
    print(sol_is_happy_number(19))  # Should print True
    print(sol_is_happy_number(2))   # Should print False
    print(sol_is_happy_number(139)) # 
    print(sol_is_happy_number(1679))