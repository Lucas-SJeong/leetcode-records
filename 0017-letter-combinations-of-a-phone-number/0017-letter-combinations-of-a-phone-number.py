class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 예외 처리: 빈 문자열이 들어온 경우
        if not digits:
            return []
            
        # 숫자별 문자 매핑 딕셔너리
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index, current_string):
            # 탐색을 끝까지 마쳐서 문자열이 완성된 경우
            if len(current_string) == len(digits):
                result.append(current_string)
                return
            
            # 현재 인덱스의 숫자에 해당하는 문자들을 가져옴
            current_digit = digits[index]
            letters = phone_map[current_digit]
            
            # 문자들을 하나씩 조합하며 재귀 호출
            for letter in letters:
                backtrack(index + 1, current_string + letter)
        
        # 0번째 인덱스, 빈 문자열 ""부터 시작
        backtrack(0, "")
        return result