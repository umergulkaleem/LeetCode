class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:


        val1 = n*n
        val2 = val1+n
        return math.gcd(val1,val2)

        # return n
        