class Solution:
    def reverseWords(self, s: str) -> str:
        news = s.split()
        ans = ""
        for i in range(len(news)-1,-1,-1):
            ans += news[i] + " "
        
        ans = ans.strip()
        return ans