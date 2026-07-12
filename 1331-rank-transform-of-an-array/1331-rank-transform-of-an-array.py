class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
  
        sortedarr = sorted(set(arr))
        rank = {}
        for i,num in enumerate(sortedarr):

            if num not in rank:
                rank[num] = i+1

        return [rank[num] for num in arr]


        
        