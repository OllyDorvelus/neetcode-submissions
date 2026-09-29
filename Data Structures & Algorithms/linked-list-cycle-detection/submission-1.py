# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_ptr, fast_ptr = head, head

        while fast_ptr:
            if fast_ptr is None or fast_ptr.next is None or fast_ptr.next.next is None:
                return False

            fast_ptr = fast_ptr.next.next

            if slow_ptr == fast_ptr:
                return True

            slow_ptr = slow_ptr.next
            



        return False 