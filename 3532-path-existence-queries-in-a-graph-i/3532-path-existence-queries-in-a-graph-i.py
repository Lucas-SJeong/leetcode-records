class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        components = [0]*n
        ans = []

        val = 0

        for i in range(1,n):
            if nums[i] - nums[i-1] > maxDiff:
                val += 1
            components[i] = val


        for u,v in queries:
            if components[u] == components[v]:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
 

        