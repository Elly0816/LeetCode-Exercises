# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Navigate through the linked list and add each nodes value to an array
        array = []
        list1 = head
        while list1:
            array.append(list1.val)
            list1 = list1.next
        # reverse the array
        array.reverse()
        # Add the values to a linked list and return the linked list
        list2 = head
        for item in array:
            list2.val = item
            list2 = list2.next
        
        return head