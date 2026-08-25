# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        maxMap = [0,0]
        level = 1
        self.findmax(root,maxMap,level)
        return maxMap[1]
        

    def findmax(self,root,maxMap,level):
        if not root:
            return

        if not root.left and not root.right:
            if level >= maxMap[0]:
                maxMap[0] = level
                maxMap[1] = root.val
        
        self.findmax(root.right,maxMap,level+1)
        self.findmax(root.left,maxMap,level+1)

            

    
        