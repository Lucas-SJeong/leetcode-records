class Solution:

    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # 1. 전체 가스의 합이 전체 비용보다 작으면 한 바퀴를 돌 수 없음
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0

        # 2. 순회하며 기름이 부족해지는 지점 확인
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            # 만약 현재까지의 잔여 가스가 음수가 되면,
            # 기존 start부터 i까지의 어떤 지점도 시작점이 될 수 없음
            if total < 0:
                start = i + 1
                total = 0

        return start