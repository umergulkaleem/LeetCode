class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap= {}
        for i, n in enumerate(nums):
            dif = target-n
            if dif in hashmap:
                return [hashmap[dif],i]
            hashmap[n]=i
        

        