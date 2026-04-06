class Solution:
    def hammingWeight(self, n: int) -> int:
        # n = format(n)
        # print(n)
        res = 0
        while n:
            res+=n % 2
            n = n >>1
        return res
        