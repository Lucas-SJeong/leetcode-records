class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans = []
        if arr[0] != 1:
            for y in range(1,arr[0]):
                ans.append(y)
                if len(ans)==k:
                    return ans[len(ans)-1]

        

        for i in range(len(arr)-1):
            if arr[i] - arr[i+1] != 1:
                for j in range(arr[i]+1, arr[i+1]):
                    ans.append(j)
                    if len(ans)==k:
                        return ans[len(ans)-1]

        print(ans)

        if k > len(ans):
            for x in range(arr[len(arr)-1]+1,arr[len(arr)-1]+k-len(ans)+1):
                ans.append(x)
                
            return ans[len(ans)-1]

        
        
        


            


        