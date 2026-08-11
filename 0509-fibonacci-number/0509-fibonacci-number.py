class Solution(object):
    def fib(self, n):
        memo = {}
        return self.memoization(n,memo)
    def memoization(self,n,memo):
        if n == 0:
            return 0
        if n == 1:
            return 1

        if n not in memo:
            memo[n] = self.memoization(n-1,memo) + self.memoization(n-2,memo)

        return memo[n]