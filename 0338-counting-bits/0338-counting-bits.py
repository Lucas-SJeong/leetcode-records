import math

class Solution(object):
    def countBits(self, n):
        arr = []
        if n==0:
            arr.append(0)
            return arr
        arr = self.countOnes(n,arr)
        arr.append(0)
        arr = arr[::-1]
        return arr
        
        
    
    def countOnes(self,n,arr):

        temp = n
        sum = 0

        if n == 1:
            arr.append(1)
            return arr
        

        while True:

            if temp == 1:
                sum += 1
                break
            elif temp == 0:
                break

            exp =  math.log(temp,2)
            greatest = pow(2,math.floor(exp))
            temp = temp - greatest
            sum += 1

            
        arr.append(sum)
        return self.countOnes(n-1,arr)
            
            
            
        