class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 0
        counter = 1
        for j in range(1,len(nums)):
            if nums[ptr] != nums[j]:
                nums[ptr+1] = nums[j]
                ptr += 1
                counter += 1
        return counter
            
            
            