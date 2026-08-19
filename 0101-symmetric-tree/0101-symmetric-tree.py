# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        arr = []
        arr1 = []
        self.postorder(root.left,arr)
        self.preorder(root.right,arr1)

        print(arr)
        print(arr1)
        return arr==arr1

    def preorder(self,root,arr):

        if not root:
            arr.append(None)
            return

        if (not root.left) and (not root.right):
            arr.append(root.val)
            return

        arr.append(root.val)
        
        self.preorder(root.left,arr)
        self.preorder(root.right,arr)


    def postorder(self,root,arr1):
        if not root:
            arr1.append(None)
            return

        if (not root.left) and (not root.right):
            arr1.append(root.val)
            return

        arr1.append(root.val)
        
        self.postorder(root.right,arr1)
        self.postorder(root.left,arr1)
        

