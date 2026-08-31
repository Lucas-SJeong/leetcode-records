class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        left,right = 0,len(nums)
        while left<right:
            mid = (left+right)//2
            if mid < nums[mid]:
                right = mid
            else:
                left =  mid+1


        if mid == nums[mid]:
            return mid+1
        elif nums[0] != 0:
            return 0

        return mid




            

        