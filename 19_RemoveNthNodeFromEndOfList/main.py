# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr, trailing = head, dummy
        
        for i in range(n - 1):
            head = head.next
            
        while head != None and head.next != None:
            head = head.next
            trailing = trailing.next
        
        trailing.next = trailing.next.next
        
        return dummy.next