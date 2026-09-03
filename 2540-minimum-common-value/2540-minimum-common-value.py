class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for n in nums1:
            left,right = 0,len(nums2)-1
            while (left<=right):
                mid = (left+right)//2
                if n < nums2[mid]:
                    right = mid -1
                elif n > nums2[mid]:
                    left = mid + 1
                elif n == nums2[mid]:
                    return n
        return -1

                
