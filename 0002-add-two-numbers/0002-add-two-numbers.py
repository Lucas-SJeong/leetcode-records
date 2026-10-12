# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        ans = ""
        temp = ""
        newnode = ListNode()
        def helper(node,ans):
            if node.next == None:
                ans += str(node.val)
                return ans
            
            ans += str(node.val)
            return helper(node.next,ans)
        
     
        temp = str(int(helper(l1,ans)[::-1]) + int(helper(l2,ans)[::-1]))
        
        base = ListNode(int(temp[len(temp)-1]))
        pointer = base
        
        for i in range(len(temp)-2,-1,-1):
            pointer.next = ListNode(int(temp[i]))
            pointer = pointer.next
            
            
        
        return base
            
            