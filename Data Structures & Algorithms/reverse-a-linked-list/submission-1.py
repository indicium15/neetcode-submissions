# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur != None:
            # Temp next
            cur_next = cur.next 
            # Assign previous
            cur.next = prev
            # Move previous up
            prev = cur
            # Move cursor to temp variable
            cur = cur_next
        return prev

        