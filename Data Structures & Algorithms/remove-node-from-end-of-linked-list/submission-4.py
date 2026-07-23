# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        node = dummy
        length = 0

        while node and node.next:
            length += 1
            node = node.next

        node = dummy
        for _ in range(length-n):
            node = node.next
        
        node.next = node.next.next
        return dummy.next


            