class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        most = max(candies)
        print(most)
        flist = []
        for i in candies:
            if i+extraCandies>=most:
                flist.append(True)
            else:
                flist.append(False)
        return flist
        