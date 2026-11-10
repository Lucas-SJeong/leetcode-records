class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slow = 0
        fast = 1
        for fast in range(len(nums)):
            if nums[fast] !=0 :
                nums[slow] = nums[fast]
                if slow != fast:
                    nums[fast] = 0
                slow += 1
          
                
                
            

