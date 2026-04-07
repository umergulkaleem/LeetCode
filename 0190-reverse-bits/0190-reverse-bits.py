class Solution:
    def reverseBits(self, n: int) -> int:
        res= ""
        n = f"{n:032b}"
        print(n)
        for i in reversed(n):
            res+=i
        return int(res,2)