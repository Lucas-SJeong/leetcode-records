# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):

        if not head or not head.next:
            return head

        else:
            current = head.next
            prev = head

        while current:
            if current.val == prev.val:
                prev.next = current.next
            else:
                prev = current
            
            current = current.next
    
        return head

          
