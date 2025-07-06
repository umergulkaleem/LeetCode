class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sor = sorted(arr)
        diff = sor[0] - sor[1]
        print(sor,"sorted")
        print(diff)
        for i in range(1,len(sor)):
            print(i,"i")
            first = sor[i]
            print(len(sor))
            if i<len(sor)-1:
                second =sor[i+1]
                print(second,"second")
                print(first,"first")
                diff1 = first - second
                print(diff1,"diff1")
                if diff != diff1:
                    return False
        return True
        