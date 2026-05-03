class Solution:
    def minSwaps(self, s: str) -> int:
        close,Mclose = 0,0

        for b in s:
            if b == "[":
                close-=1
            else:
                close+=1
            Mclose = max(close,Mclose)
        return (Mclose+1)//2
        