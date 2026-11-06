class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerS = s.lower()
        processedS = ""
        for char in lowerS:
            if (ord(char) >= 97 and ord(char) <= 122):
                processedS+=char
            elif (ord(char) >= 48 and ord(char) <= 57):
                processedS+=char

        print(processedS)
        
        for i in range(len(processedS)//2):
            if processedS[i] != processedS[len(processedS)-1-i]:
                return False

        return True
       
        

        