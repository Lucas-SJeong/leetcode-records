class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        low,high = 0,k-1
        nums.sort()
        minDiff = float('inf')
        while (high<len(nums)):
            if nums[high] - nums[low] < minDiff:
                minDiff = nums[high] - nums[low]
            low +=1
            high +=1

        return minDiff
            
        