class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sum = 0
        for i in nums:
            sum += i
        
        sum %=k
        return sum

            