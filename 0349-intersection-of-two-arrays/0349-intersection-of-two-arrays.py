class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            for j in nums2:
                if i == j:
                    if j not in ans:
                        ans.append(j)

        return ans


        