class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        count = defaultdict(int)

        res = []

        for i in nums:
            row = count[i]

            if len(res) == row:
                res.append([])
            res[row].append(i)
            count[i]+=1
        return res