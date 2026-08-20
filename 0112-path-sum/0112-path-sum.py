# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        sum = 0
        def pathsum(root,targetSum,sum):
            if not root:
                return False

            sum += root.val
            
            if (not root.left) and (not root.right):
                if sum == targetSum:
                    return True
                else:
                    return False

            

            return (pathsum(root.left,targetSum,sum) or pathsum(root.right,targetSum,sum))

        
        return pathsum(root,targetSum,sum)
            
            
            

        