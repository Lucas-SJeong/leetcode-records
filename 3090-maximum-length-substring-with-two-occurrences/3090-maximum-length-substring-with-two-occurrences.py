class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        low,high = 0,0
        hmap = {}
        length = 0
        while (high<len(s)):
            if s[high] in hmap:
                hmap[s[high]] += 1
            else:
                hmap[s[high]] = 1
            
            if hmap[s[high]] > 2:
                while (hmap[s[high]]>2):
                    hmap[s[low]] -= 1
                    low+=1
        
            high+=1
            if (high-low) > length:
                length = high-low
              
     
        return length


            
                    
            
            
        
            
        
        