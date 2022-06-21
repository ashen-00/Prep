# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(x.val, i, x.next) for i, x in enumerate(lists) if x]
        heapify(heap)
        head = dummy = ListNode()
        
        while heap:
            val, i, nextNode = heap[0]
            if not nextNode:
                heappop(heap)
            else:
                heapreplace(heap, (nextNode.val, i, nextNode.next))
            head.next = ListNode(val)
            head = head.next
            
        return dummy.next