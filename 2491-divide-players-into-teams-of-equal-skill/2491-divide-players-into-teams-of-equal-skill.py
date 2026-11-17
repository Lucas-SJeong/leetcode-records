class Solution:
    def dividePlayers(self, skill):
        # Step 1: Sort the skill array
        skill.sort()
        
        n = len(skill)
        totalSkill = skill[0] + skill[-1]  # Required sum for each pair
        chemistrySum = 0

        # Step 2: Pair players using two pointers
        for i in range(n // 2):
            # Check if the sum of current pair matches the required totalSkill
            if skill[i] + skill[n - i - 1] != totalSkill:
                return -1  # Invalid configuration, return -1
            # Calculate the chemistry (product of pair) and add it to the sum
            chemistrySum += skill[i] * skill[n - i - 1]

        return chemistrySum  # Return total chemistry