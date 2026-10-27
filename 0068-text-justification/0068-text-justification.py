class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        sntLen = 0
        prev = 0
        sentence = []
        temp = []
        ans = []
        result = ""
        
        for word in words:
            prev = sntLen
            if len(temp) == 0:
                sntLen += len(word)
            else:
                sntLen += len(word) + 1
                
            # 1. 수정: sntLen >= maxWidth 대신 sntLen > maxWidth 일 때만 이전 줄(temp)을 확정합니다.
            # (sntLen == maxWidth 인 경우는 else로 가서 temp에 담기도록 두면 마지막 줄 예외까지 한 번에 해결됩니다)
            if sntLen > maxWidth:
                sentence = temp
                temp = [word]
                sntLen = len(word)

                # 작성하신 기존 공백 분배 로직 그대로 유지
                if len(sentence) > 1:
                    gap = len(sentence) - 1
                    spaces = maxWidth - prev + gap
                    val = int(spaces / gap)
                    leftover = spaces % gap
                    result += sentence[0]
                    for i in range(1, len(sentence)):
                        if leftover > 0:
                            result += " " * (val + 1) + sentence[i]
                        else:
                            result += " " * val + sentence[i]
                        leftover -= 1

                    ans.append(result)
                else:
                    result = sentence[0] + " " * (maxWidth - len(sentence[0]))
                    ans.append(result)
                
                result = ""
            else:
                temp.append(word)

        # 2. 추가: 루프가 끝나고 temp에 남아있는 마지막 줄 처리 (왼쪽 정렬)
        if len(temp) > 0:
            result = " ".join(temp)
            result += " " * (maxWidth - len(result))
            ans.append(result)

        return ans