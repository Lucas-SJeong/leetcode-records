class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        left = 1
        right = 0
        arr = "("
        ans = []
        def helper(arr,left,right):
            if left - right < 0:
                return
            if len(arr) == 2*n:
                if left - right == 0:
                    ans.append(arr)
                return
            
            helper(arr+"(",left+1,right)
            helper(arr+")",left,right+1)

        helper(arr,left,right)
        return ans
            



        