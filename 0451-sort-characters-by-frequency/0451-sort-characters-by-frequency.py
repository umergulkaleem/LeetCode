class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = Counter(s)
        sorted_map = {k: v for k, v in sorted(hashmap.items(), key=lambda item: item[1],reverse = True)}
        print(sorted_map)
        res = ""
        for char, freq in sorted_map.items():
            res += char * freq 
        return res