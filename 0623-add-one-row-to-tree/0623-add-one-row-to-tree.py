# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        counter = 1
        if depth == 1:
            NewNode = TreeNode(val)
            NewNode.left = root
            root = NewNode
            return root
        self.addNode(root,val,depth,counter)
        return root

    def addNode(self,root,val,depth,counter):
        if not root:
            return
        
        if depth-1 == counter:
            NewNode_Left = TreeNode(val)
            NewNode_Right = TreeNode(val)
            temp =  root
    
            NewNode_Left.left = temp.left
            root.left = NewNode_Left
        
            NewNode_Right.right =  temp.right
            root.right = NewNode_Right
            
            return

        counter+=1
        self.addNode(root.left,val,depth,counter)
        self.addNode(root.right,val,depth,counter)
            
                
            

        
      