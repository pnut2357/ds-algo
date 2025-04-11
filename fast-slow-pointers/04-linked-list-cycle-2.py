"""
https://leetcode.com/problems/linked-list-cycle-ii/description/
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detect_cycle(head: ListNode) -> ListNode:
    """
    Args:
        head: ListNode
    Returns:
        The node where the cycle begins.
    Algo:
        1. Use two pointers to find the cycle.
        2. if two pointers meet, it is cyclic.
        3. if not, return None. 
        
    """
    cur = head
    lookup = {}
    while cur:
        if cur in lookup:
            return cur
        lookup[cur] = cur.val
        cur = cur.next
    return None

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    print(detect_cycle(head))

    head.next.next.next.next.next.next = head.next.next
    print(detect_cycle(head).val)
    # slow, fast = head, head
    # while fast and fast.next:
    #     slow = slow.next
    #     fast = fast.next.next
    #     if slow == fast:
    #         break
            