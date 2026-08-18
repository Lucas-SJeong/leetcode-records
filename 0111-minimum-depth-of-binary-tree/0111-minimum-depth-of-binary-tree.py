# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):

        sum = 1
        if not root:
            return 0
        if (root.left is None) and (root.right is None):
            return 1


        return min(self.depth(root.left,sum),self.depth(root.right,sum))
        
    def depth(self,root,sum):
        
        if not root:
            return float('inf')
        if (root.left is None) and (root.right is None):
            return sum+1


        sum += 1

        return min(self.depth(root.left,sum),self.depth(root.right,sum))

       