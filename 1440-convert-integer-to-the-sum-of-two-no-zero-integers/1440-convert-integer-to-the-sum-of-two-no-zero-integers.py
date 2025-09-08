class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        def has_zero(x):

            return "0" in str(x)

        for i in range(1,n):
            first,second = i,n-i
            if not has_zero(first) and  not has_zero(second):
                return [first,second]


        
        