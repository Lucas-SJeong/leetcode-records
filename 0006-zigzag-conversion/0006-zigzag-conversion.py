class Solution:
    def convert(self, s: str, numRows: int) -> str:
        gap = numRows * 2
        crntpos = 0
        ans = ""
        part = -2
        converted = True

        # 수정된 부분: numRows가 1이거나 문자열 길이 이상일 때는 지그재그가 의미 없으므로 원본 반환
        if numRows == 1 or len(s) <= numRows:
            return s

        for i in range(numRows):
            gap -= 2
            part += 2
            crntpos = i
            while crntpos < len(s):
                ans += s[crntpos]
                if gap == 0:
                    crntpos += part
                elif part == 0:
                    crntpos += gap
                else:
                    if not converted:
                        crntpos += part
                        converted = True
                    else:  
                        crntpos += gap
                        converted = False

            converted = True
        return ans

                
                
        