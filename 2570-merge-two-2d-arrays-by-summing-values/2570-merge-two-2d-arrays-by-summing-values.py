class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # p1 = 0
        # p2 = 0

        # p1hash = set()
        # for i,j in nums1:
        #     p1hash.add(i)
        # print(p1hash)
        # p2hash = set()
        # for i,j in nums2:
        #     p2hash.add(i)
        # print(p2hash)
        # res = []
        # while p1<len(nums1) and p2 < len(nums2):
        #     num1 = nums1[p1][0]
        #     num2 = nums2[p2][0]
        #     if num1 == num2:
        #         res.append([num1,nums1[p1][1]+nums2[p2][1]])
        #         p1+=1
        #         p2+=1
        #     elif num1<num2:
        #         res.append([num1,nums1[p1][1]])
        #         p1+=1
        #     else:
        #         res.append([num2,nums2[p2][1]])
        #         p2+=1
        #     print(p1,p2)
        # return res
        mp = defaultdict(int)

        for i, v in nums1:
            mp[i] += v
        for i, v in nums2:
            mp[i] += v

        return sorted([[k, v] for k, v in mp.items()])
            
             


        