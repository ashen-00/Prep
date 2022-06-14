# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while True:
            # reached a None node, AKA previously, self.next = None
            if not head:
                return False
            # val is None, which means we've been here before
            if not head.val:
                return True
            head.val = None
            head = head.next