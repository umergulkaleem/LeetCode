class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        res = []
        for i in hashmap:
            print(i)
            if hashmap[i] >1:
                res.append(i)
        return res
        