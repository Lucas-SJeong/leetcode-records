class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s = s + "E"
        prev = 0
        curr = 1
        ans = 0
        for x in range(1,len(s)):
            if (s[x-1] != s[x]):
                ans += min(prev,curr)
                prev = curr
                curr = 1
            else:
                curr += 1
        return ans
            
            