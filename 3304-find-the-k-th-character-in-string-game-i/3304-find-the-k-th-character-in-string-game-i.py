class Solution(object):
    def kthCharacter(self, k):
        
        arr =  ['a']
        rpt = 0
        return self.characters(k,arr)
        
    
    def characters(self,k,arr):

        if len(arr)>=k:
            return arr[k-1]
        
        temp = []

        for i in arr:
            temp.append(chr(ord(i)+1))

        arr += temp
        return self.characters(k,arr)

        

        