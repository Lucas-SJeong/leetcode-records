class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left,right = 0,3
        set_ans = {}
        count = 0
        while(right<len(s)+1):
            if len({s[left],s[left+1],s[left+2]}) == 3:
        
                count += 1
                
                
            left+=1
            right+=1
        
        return count