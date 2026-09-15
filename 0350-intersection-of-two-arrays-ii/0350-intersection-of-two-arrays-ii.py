class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = {}
        ans2 = {}
        final = []
        counter = 0
        if len(nums1) < len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp

        for num in nums2:
            print(num)
            if num not in ans:
                ans[num] = 1
            else:
                ans[num] += 1

        for element in nums1:
            if element in ans:
                if ans[element] > 0:
                    ans[element] -= 1
                    final.append(element)

        return final           
                     

            
            
            
            