class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        next = 0
        if len(s) == 0:
            return True

        for i in t:
            if i == s[next]:
                next += 1
                if next == len(s):
                    return True

        return False


            
        
        