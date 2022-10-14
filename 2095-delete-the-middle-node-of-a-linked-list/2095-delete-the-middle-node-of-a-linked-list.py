# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return 
        slowl = head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slowl = slow
            slow = slow.next
            fast = fast.next.next
        if fast.next:
            slowl = slow
            slow = slow.next
        slowl.next = slow.next
        return head