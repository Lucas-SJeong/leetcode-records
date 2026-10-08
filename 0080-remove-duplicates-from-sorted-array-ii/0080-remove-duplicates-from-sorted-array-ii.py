class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pointer= 1
        dup_cnt = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                dup_cnt += 1
            else:
                dup_cnt = 1
            
            if dup_cnt <= 2:
                nums[pointer] = nums[i]
                pointer += 1
        
        return pointer