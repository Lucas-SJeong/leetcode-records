# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class EscapeRecursion(Exception): 
    pass


class Solution(object):
    def isBalanced(self, root):
        
        num = 1
        try:
            self.tree(root,num)
        except EscapeRecursion as e:
            return False

        return True

    def tree(self,root,num):

        
        if not root:
            return num-1

        if (not root.left) and (not root.right):
            return num

        left = self.tree(root.left,num+1)
        right = self.tree(root.right,num+1)

        if abs(left-right)<=1:
            return max(left,right)
        else:
            raise EscapeRecursion()
        