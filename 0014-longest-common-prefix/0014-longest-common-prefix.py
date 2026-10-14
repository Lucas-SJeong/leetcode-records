class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest = min(strs, key=len)
        found = False
        latest = 0

        if len(strs) == 1:
            return strs[0]

        for x in range(0,len(shortest)):
            for element in strs:
                if element[:x+1] != shortest[:x+1]:
                    return element[:latest]
                
            latest = x+1
        
        return shortest[:latest]
                    



                
            

     


