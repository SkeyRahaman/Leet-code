# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        count =0
        while ptr.next:
            ptr = ptr.next
            count += 1
        d = count-n+1
        if d == 0:
            return head.next
        count = 0
        last = head
        ptr = last.next
        while count != d-1:
            count += 1
            last = ptr
            ptr = ptr.next
        last.next = ptr.next
        return head
        
        