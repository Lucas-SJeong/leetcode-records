class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hashs = {}
        for element in nums:
            if element not in hashs:
                hashs[element] = 1
            else:
                hashs[element] += 1
            
            if hashs[element] >= (len(nums)/2):
                    return element
            
            
                
        