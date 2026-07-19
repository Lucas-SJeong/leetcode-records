class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def backtrack(current_string, open_count, close_count):
            # 여는 괄호와 닫는 괄호가 모두 n개씩 쓰여서 완성된 경우
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            # 1. 여는 괄호를 더 쓸 수 있는 경우 추가
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
                
            # 2. 닫는 괄호가 여는 괄호 개수보다 적게 쓰인 경우에만 추가 가능
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)
        
        # 빈 문자열 "", 여는 괄호 0개, 닫는 괄호 0개 상태로 시작
        backtrack("", 0, 0)
        return result