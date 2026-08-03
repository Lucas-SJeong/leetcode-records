class Solution(object):
    def searchInsert(self, nums, target):
        notfound = True
        low = 0
        high = len(nums) -1
        mid = (len(nums)-1)//2
      

        while notfound:


            if target==nums[mid]:
                return mid
            elif (low + 1 == high or high == low):
                if target < nums[low]:
                    return 0
                elif target > nums[high]:
                    return high + 1
                elif (target <= nums[high]):
                    return high
            elif target > nums[mid]:
                low = mid
                mid = (low+high)//2
            elif target < nums[mid]:
                high = mid
                mid = (low+high)//2
    
            
        
        
            
            
            
            

        