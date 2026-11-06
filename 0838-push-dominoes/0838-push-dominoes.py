class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        force = len(dominoes)
        right,left = 0,len(dominoes)-1
        forceMap = [0]*force
        ans = ""

        while (right<len(dominoes)):
            if dominoes[right] == "R":
                forceMap[right] = force
                right += 1
                while (right<len(dominoes)and (dominoes[right] == ".")):
                    force -= 1
                    forceMap[right] = force
                    right += 1
                force = len(dominoes)
            else:
                right+=1

        force = len(dominoes)

        while (left>=0):
            if dominoes[left] == "L":
                forceMap[left] -= force
                left -= 1
                while (left>=0 and (dominoes[left] == ".")):
                    force -= 1
                    forceMap[left] -= force
                    left -= 1
                force = len(dominoes)
            else:
                left -= 1

        for x in forceMap:
            if x == 0:
                ans += "."
            elif x < 0:
                ans += "L"
            else:
                ans += "R"

        return ans

      