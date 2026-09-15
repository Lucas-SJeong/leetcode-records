class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr1 = 0
        ptr2 = len(nums)-1
        temp = 0

        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1

        while (ptr1<ptr2):
            if nums[ptr1] == val:
                if nums[ptr2] == val:
                    ptr2 -= 1
                else:
                    temp = nums[ptr2]
                    nums[ptr2] = nums[ptr1]
                    nums[ptr1] = temp

                    ptr1+=1
                    ptr2-=1
            else:
                ptr1+=1


        if ptr1==0:
            return 0

        if nums[ptr2] == val:
            return ptr2
        else:
            return ptr2 + 1

        
                

            
                
                
            
            
        