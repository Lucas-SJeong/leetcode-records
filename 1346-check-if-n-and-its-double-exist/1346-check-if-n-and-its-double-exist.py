class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        counter = 0
        for num in arr:
            if (num%2 == 0):
                copy = arr[:counter] + arr[counter+1:]
                print(copy)
                target = num/2
                left,right = 0,len(copy)-1
                while (left<=right):
                    mid = (left+right)//2
                    if copy[mid] < target:
                        left = mid + 1
                    elif copy[mid] > target:
                        right = mid - 1
                    elif (copy[mid] == target):
                        return True
            counter+=1
            
        return False


                
        