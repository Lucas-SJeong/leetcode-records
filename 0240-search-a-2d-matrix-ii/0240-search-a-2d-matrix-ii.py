class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for mat in matrix:
            left,right = 0,len(mat)-1
            while (left<=right):
                mid = (left+right)//2
                if mat[mid] == target:
                    return True

                if mat[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

        return False