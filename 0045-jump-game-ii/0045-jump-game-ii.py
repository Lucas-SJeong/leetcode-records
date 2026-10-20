class Solution:
    def jump(self, nums: list[int]) -> int:
        left = 0
        count = 0
        greatest = 0
        right = 0
        while (right<len(nums)-1):
            greatest = 0
            for i in range(left,right+1):
                greatest = max(greatest,i+nums[i])
            left = right
            right = greatest
            count+=1
        
        return count