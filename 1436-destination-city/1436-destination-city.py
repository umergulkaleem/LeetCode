class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        first = set()
        second = set()
        for i,j in paths:
            first.add(i)
            second.add(j)
        
        for i,j in paths:
            if j not in first:
                return j
                
        