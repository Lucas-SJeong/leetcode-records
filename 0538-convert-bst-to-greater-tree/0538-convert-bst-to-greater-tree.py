# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current_sum = 0

        # 내부 함수이므로 self 제거
        def postOrderSum(node):
            nonlocal current_sum
            if not node:
                return

            postOrderSum(node.right)

            current_sum += node.val
            node.val = current_sum  # sum -> current_sum으로 수정

            postOrderSum(node.left)

        postOrderSum(root)
        return root