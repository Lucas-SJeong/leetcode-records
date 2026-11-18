class Solution:
    def getStrongest(self, arr: list[int], k: int) -> list[int]:
        arr.sort()
        print(arr)
        left,right = 0,len(arr)-1
        mid = right//2
        ans = []
        counter = 0

        if len(arr) == 1:
            return arr


        while(counter<k):
        
    
            if abs(arr[left] - arr[mid]) > abs(arr[right]-arr[mid]):
                ans.append(arr[left])
                left+=1
                counter+=1
            elif abs(arr[left] - arr[mid]) < abs(arr[right]-arr[mid]):
                ans.append(arr[right])
            
                right-=1
                counter+=1
            else:
                ans.append(arr[right])
           
                right-=1
                counter+=1
        return ans


    