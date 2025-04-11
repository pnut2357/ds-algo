"""
https://leetcode.com/problems/middle-of-the-linked-list/description/
Given the head of a singly linked list, return the middle node of the linked list.
if there are two middle nodes, return the second middle node.
i.e.
Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle_of_the_linked_list(head: ListNode) -> ListNode:
    """
    Args:
        head: ListNode
    Returns:
        The middle node of the linked list.
    Algo:
        Use two pointers to find the middle node. 
    """
    count = 0
    temp = head
    while temp:
        temp = temp.next
        count += 1
    count = count // 2 + 1
    ptr = head
    for _ in range(count-1):
        ptr = ptr.next
        # count -= 1
    return ptr

def sol_middle_of_the_linked_list(head: ListNode) -> ListNode:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def sol_2_middle_of_the_linked_list(head: ListNode) -> ListNode:
    """Array based solution
    """
    arr = [head]
    while arr[-1].next:
        arr.append(arr[-1].next)
    return arr[len(arr)//2]

def print_linked_list(head: ListNode):
    temp = head
    while temp:
        print(temp.val, end=" ")
        temp = temp.next
    print()

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print_linked_list(middle_of_the_linked_list(head))
    print_linked_list(sol_middle_of_the_linked_list(head))
    print_linked_list(sol_2_middle_of_the_linked_list(head))
    head.next.next.next.next.next = ListNode(6)
    print_linked_list(middle_of_the_linked_list(head))
    print_linked_list(sol_middle_of_the_linked_list(head))
    print_linked_list(sol_2_middle_of_the_linked_list(head))