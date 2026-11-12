class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        left,right = 0,len(s)-1
        sList = list(s)
        print(sList[left].isalpha())
        while(left<right):
            if not(sList[left].isalpha())or not(sList[right].isalpha()):
                if not sList[left].isalpha():
                    left+=1
                else:
                    right-=1
            else:
                temp = sList[right]
                sList[right] = sList[left]
                sList[left] = temp
                left += 1
                right -= 1
        ans = "".join(sList)
        return ans
            
                