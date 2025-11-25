class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        remainder = 1 % k
        length = 1
        # iterate up to k times (pigeonhole)
        while remainder != 0 and length <= k:
            remainder = (remainder * 10 + 1) % k
            length += 1

        return length if remainder == 0 else -1
        