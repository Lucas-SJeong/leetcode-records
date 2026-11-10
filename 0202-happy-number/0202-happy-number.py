class Solution:
    def isHappy(self, n: int) -> bool:
        slow = -1
        fast = -1
        hNum = n
        ans = []
        flag = False
        while (hNum!=1):

            strNum = str(hNum)
            hNum = 0
            for x in strNum:
                hNum += int(x)**2
              
            ans.append(hNum)
    
            if flag == True:
                slow += 1
                fast += 2
                if ans[slow] == ans[fast]:
                    return False
                flag = False
            else:
                flag = True
            
            

        return True         


                
            
            
        