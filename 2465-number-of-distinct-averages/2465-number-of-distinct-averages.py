class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        distinct_avg = set()
        def helper(distinct_avg,nums):
            if len(nums) == 0:
                return
            minIdx = nums.index(min(nums))
            maxIdx = nums.index(max(nums))
            avg = (nums[minIdx] + nums[maxIdx])/2
            distinct_avg.add(avg)
            nums.pop(minIdx)
            if minIdx > maxIdx:
                nums.pop(maxIdx)
            else:
                nums.pop(maxIdx-1)
            helper(distinct_avg,nums)
        
        helper(distinct_avg,nums)
        return len(distinct_avg)
            
            
            
        