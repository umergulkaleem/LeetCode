class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res= []
        for i in nums:
            res.append(i*i)
        # print(res)
        return sorted(res)

        