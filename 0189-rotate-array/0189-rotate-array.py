class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        rotation = k%len(nums)

        left = nums[len(nums)-rotation:]
        right = nums[:len(nums)-rotation]
        ans = left+right
        if k!=0:
            for i in range(len(nums)):
                nums[i] = ans[i]
        
            