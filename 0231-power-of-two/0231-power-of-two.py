class Solution(object):
    def isPowerOfTwo(self, n):
        
        return self.validate(n)

    def validate(self,n):
        if n==0:
            return False

        if (n%2==1 and n!=1):
            return False

        if n==2 or n==1:
            return True
        
        return self.validate(n/2)

        