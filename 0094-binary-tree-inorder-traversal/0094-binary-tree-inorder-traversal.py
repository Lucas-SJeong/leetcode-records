# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        temp = []
        def helper(root):
            if root is None:
                
                return
            
            elif not root.left and not root.right:
                temp.append(root.val)
                return
            
            helper(root.left)
            temp.append(root.val)
            helper(root.right)
            
            

        helper(root)
        return temp
        