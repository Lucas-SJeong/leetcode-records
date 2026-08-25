# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        hashMap = {}
        level = 1
        self.findVal(root,level,hashMap)
        ans = [i[0] for i in hashMap.values()]
        return ans
        

    def findVal(self,root,level,hashMap):

        if not root:
            return

        if level not in hashMap:
            hashMap[level] = [root.val]
        else:
            if root.val > hashMap[level][0]:
                hashMap[level] = [root.val]
        
        self.findVal(root.left,level+1,hashMap)
        self.findVal(root.right,level+1,hashMap)

                
        

        
        

        
        
        