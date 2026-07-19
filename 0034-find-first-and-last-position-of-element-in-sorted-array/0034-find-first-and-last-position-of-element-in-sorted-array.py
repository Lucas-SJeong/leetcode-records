class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findBound(is_first):
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if is_first:
                        # 첫 번째 위치를 찾으려면 왼쪽 영역을 계속 탐색
                        right = mid - 1
                    else:
                        # 마지막 위치를 찾으려면 오른쪽 영역을 계속 탐색
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound

        # 첫 번째 위치와 마지막 위치를 각각 이진 탐색으로 찾음
        first_pos = findBound(is_first=True)
        last_pos = findBound(is_first=False)
        
        return [first_pos, last_pos]