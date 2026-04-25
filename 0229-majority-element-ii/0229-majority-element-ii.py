class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)//3
        # print(round(n))      

        hashmap = Counter(nums)
        res = []

        for i in hashmap.keys():
            if hashmap[i] > n:
                res.append(i)
        return res 