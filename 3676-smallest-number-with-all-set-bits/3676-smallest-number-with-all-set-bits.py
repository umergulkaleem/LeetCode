class Solution:
    def smallestNumber(self, n: int) -> int:
        while True:
            curr = bin(n)[2:]
            print(curr)
            if all(x=="1" for x in curr):
                return n
            n+=1
        