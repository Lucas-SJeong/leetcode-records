class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        x = list(x)
        counter = 0
        xReversed = x[::-1]
        for i in x:
            if xReversed[counter] != i:
                return False
            counter+=1
        return True
            
            
        