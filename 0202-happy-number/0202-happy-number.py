class Solution:
    def isHappy(self, n: int) -> bool:
        slow = -1
        fast = -1
        hNum = n
        temp = 0
        ans = []
        flag = False
        while (hNum!=1):

            strNum = str(hNum)

            for x in strNum:
                temp += int(x)**2
              
            hNum = temp
            ans.append(hNum)
            temp = 0
    
            if flag == True:
                slow += 1
                fast += 2
                if ans[slow] == ans[fast]:
                    return False
                flag = False
            else:
                flag = True
            
            

        return True         


                
            
            
        