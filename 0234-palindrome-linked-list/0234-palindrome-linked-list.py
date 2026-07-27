# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import copy
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:


        head_copy = copy.deepcopy(head)
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        


        current1 = head_copy
        current2 = prev

        while current1:
            if current1.val == current2.val:
                current1 = current1.next
                current2 = current2.next
            else:
                return False
            

        return True
        