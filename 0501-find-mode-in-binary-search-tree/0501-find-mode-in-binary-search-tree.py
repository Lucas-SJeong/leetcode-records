from collections import Counter

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        arr = []
        self.finder(root,arr)
        counts = Counter(arr)
        max_count = max(counts.values())
        most_frequent_items = [item for item, count in counts.items() if count == max_count]
        return most_frequent_items
        
    def finder(self,root,arr):
        if not root:
            return

        self.finder(root.left,arr)
        arr.append(root.val)
        self.finder(root.right,arr)

        
        
                
                

       
        

        

        
        