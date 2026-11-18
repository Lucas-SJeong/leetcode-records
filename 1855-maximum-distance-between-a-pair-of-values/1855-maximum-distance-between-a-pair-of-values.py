class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        maxDist = 0
        left,right = len(nums1)-1, len(nums2)-1
        while (left >=0 and right >= 0):
            if left > right:
                left-=1
                continue

            if nums1[left] <= nums2[right]:
                maxDist = max(maxDist,right-left)
                left-=1
            else:
                right-=1
        return maxDist