class Solution(object):
    def letterCombinations(self, digits):
        numDict = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
            }
        
        ans = []
        depth = len(digits)-1
        crntString = ""
        pointer = 0

        def helper(pointer,crntString):
            if pointer > depth:
                ans.append(crntString)
                return

            for word in numDict[digits[pointer]]:
                helper(pointer+1,crntString+word)
            
        helper(pointer,crntString)
        return ans
            

                
                
                
        