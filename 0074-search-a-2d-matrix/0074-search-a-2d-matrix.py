class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bottom = 0, len(matrix)-1
        left,right = 0, len(matrix[0])-1
        temp = []
        while (top<=bottom):
            mid = (top+bottom)//2
            if matrix[mid][0] <= target and matrix[mid][len(matrix[0])-1] >= target:
                temp = matrix[mid]
                break
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                top = mid + 1
        
        if len(temp) == 0:
            return False


        while (left<=right):
            mid = (left+right)//2
            if temp[mid] == target:
                return True
            if temp[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
                
            

            
            
        
        

            

            

        
            

        