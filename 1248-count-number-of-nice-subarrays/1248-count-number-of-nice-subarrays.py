class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        left = 0
        odd = 0
        count = 0
        prefix_evens = 0  # 현재 유효 윈도우의 왼쪽에 위치한 짝수 개수

        for right in range(len(nums)):
            # 1. 오른쪽 포인터가 홀수를 만나면 odd 증가
            if nums[right] % 2 != 0:
                odd += 1
                prefix_evens = 0  # 새로운 홀수가 들어왔으므로 이전 홀수 기준의 짝수 카운트 리셋

            # 2. 홀수가 k개를 초과하면 left를 이동시켜 윈도우 축소
            while odd > k:
                if nums[left] % 2 != 0:
                    odd -= 1
                left += 1

            # 3. 홀수가 정확히 k개일 때: 왼쪽의 짝수들을 건너뛰며 유효 시작점 수 계산
            if odd == k:
                while nums[left] % 2 == 0:
                    prefix_evens += 1
                    left += 1
                # (기본 1개 + 건너뛴 짝수 개수)만큼 부분 배열 형성 가능
                count += (prefix_evens + 1)

        return count
        

            