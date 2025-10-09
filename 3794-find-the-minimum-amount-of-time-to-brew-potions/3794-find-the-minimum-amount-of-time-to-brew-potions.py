class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        
        sumSkill = sum(skill)
        prevWizardDone = sumSkill * mana[0]  # End time after first potion passes all wizards
        
        for j in range(1, len(mana)):
            prevPotionDone = prevWizardDone
            for i in range(len(skill) - 2, -1, -1):
                # Calculate earliest possible start time based on previous timings and synchronization
                prevPotionDone -= skill[i + 1] * mana[j - 1]
                prevWizardDone = max(prevPotionDone, prevWizardDone - skill[i] * mana[j])
            prevWizardDone += sumSkill * mana[j]  # Add total skill time for current potion
        
        return prevWizardDone