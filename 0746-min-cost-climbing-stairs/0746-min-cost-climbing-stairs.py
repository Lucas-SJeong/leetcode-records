class Solution(object):
    def minCostClimbingStairs(self, cost):

        memo = {}
        n = len(cost)-1
        return min(self.findstairs(cost,memo,n),self.findstairs(cost,memo,n-1))
    

    def findstairs(self,cost,memo,n):

        if n<0:
            return 0

        if n in memo:
            return memo[n]

        memo[n] = cost[n] + min(self.findstairs(cost,memo,n-1),self.findstairs(cost,memo,n-2))
        
        

        return memo[n]