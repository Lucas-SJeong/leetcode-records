import math

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for j in range(len(nums)-1,-1,-1):
            ans[j] *= suffix
            suffix *= nums[j]
        return ans
            