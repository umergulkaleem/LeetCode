class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        pairs = []

        for i,n in enumerate(nums):
            n = str(n)
            mapping_n = 0
            for j in n:
                mapping_n*=10
                mapping_n +=mapping[int(j)]
            pairs.append((mapping_n,i))

        pairs.sort()

        return[nums[p[1]] for p in pairs]        