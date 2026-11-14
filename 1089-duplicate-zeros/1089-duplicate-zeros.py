class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        close = len(arr)-1
        zeros = 0
        for i in arr:
            if i == 0:
                zeros += 1
        far = close + zeros
        while(close<far):
            if far < len(arr):
                arr[far] = arr[close]
                if arr[close] == 0:
                    far -= 1
                    arr[far] = 0
                    print(far)
            else:
                if arr[close] == 0:
                    far -= 1
                    if far<len(arr):
                        arr[far] =0
                    
            far-=1
            close-=1
                
                
                
            
    
                
                




