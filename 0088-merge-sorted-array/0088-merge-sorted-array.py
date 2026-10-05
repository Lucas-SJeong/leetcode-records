class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        outer = m - 1
        inner = n - 1
        total = m+n-1
        while(inner>=0):
            if outer >= 0 and nums1[outer] > nums2[inner]:
                nums1[total] = nums1[outer]
                outer -= 1 
            else:
                nums1[total] = nums2[inner]
                inner -=1
            total -=1
            