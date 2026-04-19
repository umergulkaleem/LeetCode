class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashmap  = Counter(arr1)
        ans = []
        for  i in arr2:
            if i in hashmap:
                ans.extend([i]*hashmap[i])
                del (hashmap[i])
        for i in sorted(hashmap):
            ans.extend([i]*hashmap[i])
        return ans