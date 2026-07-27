# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        loop = False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                loop = True
                break
            
                     
        if loop == True:
            bottom = head
            while fast != bottom:
                bottom = bottom.next
                fast = fast.next
            
            return bottom
            
            

        