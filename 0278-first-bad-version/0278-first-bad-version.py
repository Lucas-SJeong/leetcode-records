# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        low = 1
        high = n
        mid = low + high // 2
        notfound = True
        
        if isBadVersion(1) == True:
            return 1

        while notfound:
            if (low + 1 == high) or (low==high):
                return high
            elif isBadVersion(mid) == False:
                low = mid
                mid = (low + high) // 2
            elif isBadVersion(mid) == True:
                high = mid
                mid = (low + high) //2


            


            
        