class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        if n == 0:
            return []
            
        group_id = [0] * n
        current_id = 0
        
        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                current_id += 1
            group_id[i] = current_id
            
        answer = []
        for u, v in queries:
            answer.append(group_id[u] == group_id[v])
            
        return answer
        