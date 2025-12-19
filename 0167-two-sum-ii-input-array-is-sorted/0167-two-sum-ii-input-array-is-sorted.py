class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a,b = 0,len(numbers)-1
        sumof = 0
        while a<b:
            sumof= numbers[a]+numbers[b]
            if sumof > target:
                b-=1
            elif sumof<target:
                a+=1
            else:
                return [a+1,b+1]
        