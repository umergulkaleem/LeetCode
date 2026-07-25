class Solution:
    def maxProduct(self, n: int) -> int:
        arr = []
        print(n%10)
        while n:
            arr.append(n%10)
            n = n//10
        arr.sort()
        return arr[-1]*arr[-2]