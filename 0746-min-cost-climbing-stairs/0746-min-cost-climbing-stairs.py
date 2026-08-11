class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        # dp[i]: i번째 계단까지 도달하는 데 드는 최소 비용
        dp = [0] * (n + 1)
        
        # 0번째, 1번째 계단은 시작점이므로 도달 비용이 0
        dp[0] = 0
        dp[1] = 0
        
        for i in range(2, n + 1):
            # (1칸 전에서 올라오는 비용)과 (2칸 전에서 올라오는 비용) 중 최소값 선택
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
            
        return dp[n]