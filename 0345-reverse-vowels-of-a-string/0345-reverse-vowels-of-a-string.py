class Solution:
    def reverseVowels(self, s: str) -> str:
        set = {"A","E","I","O","U","a","e","i","o","u"}
        listS = list(s)
        ans = ""
        left,right = 0, len(s)-1
        while(left<right):
            if listS[left] in set and listS[right] in set:
                temp = listS[right]
                listS[right] = listS[left]
                listS[left] = temp
                left += 1
                right -=1
            elif listS[left] in set:
                right -=1
            elif listS[right] in set:
                left += 1
            else:
                left += 1
                right -= 1
        for i in range(len(s)):
            ans += listS[i]
        return ans