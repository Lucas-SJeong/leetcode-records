class Solution(object):
    def romanToInt(self, s):
        s = list(s)
        skipper = False
        summed = 0
        diction =  {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)):
            if skipper == True:
                skipper = False
                continue
            if i!=len(s)-1:
                if s[i] == "I" and (s[i+1] == "V"  or s[i+1] == "X"):
                    summed += diction[s[i+1]] - diction[s[i]]
                    skipper = True
                elif s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                    summed += diction[s[i+1]] - diction[s[i]]
                    skipper = True
                elif s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"):
                    summed += diction[s[i+1]] - diction[s[i]]
                    skipper = True
                else:
                    summed += diction[s[i]]
                    skipper = False
            else:
                summed += diction[s[i]] 
        return summed

             
                     
            
            