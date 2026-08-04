class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a = min(nums)
        b = max(nums)
        need = []
        have = set(nums)
        count = a
        while count!=b:
            count+=1
            if count not in have:
                need.append(count)
        return need

        