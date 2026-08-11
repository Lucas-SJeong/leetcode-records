class Solution(object):
    def tribonacci(self, n):

        memo = {}
        return self.bona(n,memo)


    def bona(self,n,memo):
        if (n == 1) or (n == 2):
            return 1
        elif n == 0:
            return 0
        
        if n in memo:
            return memo[n]
        else:
            memo[n] = self.bona(n-1,memo) + self.bona(n-2,memo) + self.bona(n-3,memo)

        
        return memo[n]
        
        
        
        

        
        