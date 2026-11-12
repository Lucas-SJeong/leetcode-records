class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        left, right =  0, len(nums)-1
        while (left<=right):
            while(left<=right):
                if abs(left - right) >= indexDifference and abs(nums[left]-nums[right]) >= valueDifference:
                    return [left,right]
                right-=1

            left += 1
            right = len(nums) -1

        return [-1,-1]
        
            
                    
        