# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        count = 0
        start1 = head
        
        find = 0
        
        while start1:
            count += 1
            start1 = start1.next
            
        print(f"the linked list has {count} entries")
        if (count/2) == int(count/2):
            print(count)
            find = (count/2) +1
            print('int');
        else:
            find = (count/2) + 0.5
            print(count)
            print('not int')
        
        
        start2 = head
        print(find)
        for i in range(int(find)-1):
            start2 = start2.next
        
        return start2