# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        

        def invert(root):

            if not root:
                return

            if (not root.left) and (not root.right):
                return
            
            invert(root.left)
            invert(root.right)

            temp = root.left
            root.left = root.right
            root.right = temp

        invert(root)
        return root




    
