class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentL= sentence.split()
        counter = 0
        for elem in sentL:
            counter += 1
            if len(elem) >= len(searchWord):
                found = True
                for i in range(len(searchWord)):
                    if elem[i] != searchWord[i]:
                        found = False
                        break
                if found == True:
                    return counter 
                    

            
        return -1

            
            
        