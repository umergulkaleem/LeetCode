class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        totalPairs = 0
        goodPairs = 0
        count = defaultdict(int)

        for i in range(len(nums)):
            totalPairs+=i
            goodPairs+=count[nums[i]-i]
            count[nums[i]-i]+=1
        return totalPairs-goodPairs