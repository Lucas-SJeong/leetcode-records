# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):

        if not root:
            return False

        if root.val == subRoot.val:
            if self.subtree(root,subRoot):
                return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        

    def subtree(self,root,subRoot):

        if (not root and not subRoot):
            return True
        elif (not root)and(subRoot):
            return False
        elif (not subRoot) and (root):
            return False

        if not (root.val == subRoot.val):
            return False

        return (self.subtree(root.left,subRoot.left) and self.subtree(root.right,subRoot.right))
        
        