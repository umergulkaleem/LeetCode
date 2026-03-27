class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        map1 ={}

        for i,ch in enumerate(s):
            
                map1[ch]=i
        
        size = 0
        end =0
        # while start = len(s):
        #     if map1[start] > end:
        #         end = map1[start]
        res= []
        for i,ch in enumerate(s):
            if map1[ch]>end:
                end = map1[ch]
            
            size+=1
            if end == i:
                res.append(size)
                size= 0
        return res
        