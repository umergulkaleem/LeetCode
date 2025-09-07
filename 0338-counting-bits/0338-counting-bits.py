class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)  # initialize result array with zeros
        for i in range(1, n + 1):
            # ans[i >> 1] gives count of 1s in i//2
            # (i & 1) is 1 if i is odd, 0 if i is even
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
        