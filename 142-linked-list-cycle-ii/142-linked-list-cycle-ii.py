# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## Tortoise and the hare algorithm
        slow = head
        fast = head
        
        # The linked list is empty
        if not fast:
            return None
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow: 
                break
        
        ## We are at the end of the linked list
        if not fast.next or not fast.next.next:
            return None
        
        ## start another pointer at the head
        slow2 = head
        
        ## If slow2 and slow are the same return slow
        ## Here we know that a cycle exists and 
        while True:
            if slow == slow2:
                return slow
            slow = slow.next
            slow2 = slow2.next
        
        