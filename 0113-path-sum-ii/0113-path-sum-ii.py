# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        local_arr = []
        global_arr = []
        self.summed(root,targetSum,local_arr,global_arr)
        return global_arr
    def summed(self,root,targetSum,local_arr,global_arr):
        if not root:
            return
        
        local_arr.append(root.val)

        if (not root.left) and (not root.right):
            if sum(local_arr) == targetSum:
                global_arr.append(local_arr)
                return

        self.summed(root.left,targetSum,local_arr[:],global_arr)
        self.summed(root.right,targetSum,local_arr[:],global_arr)

