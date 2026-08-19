class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        
        ans = 0
        # 왼쪽 자식이 잎 노드인지 확인
        if root.left and not root.left.left and not root.left.right:
            ans = root.left.val
        
        # 좌/우 서브트리의 왼쪽 잎 합을 더해서 반환
        return ans + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)



        
        