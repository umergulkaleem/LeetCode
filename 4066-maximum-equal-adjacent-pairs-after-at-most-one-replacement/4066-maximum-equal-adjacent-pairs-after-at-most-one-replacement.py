class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:

        # count = Counter(nums)
        # print(count)
        # maxnum = max(count, key=count.get)
        # print(maxnum)
        # pairs = 0
        # came = False
        # prev = nums[0]

        # for i in range(1,len(nums)):
        #     curr = nums[i]
        #     print(prev,curr)
        #     if prev == maxnum:
        #         print("first in")
        #         if curr == maxnum:
        #             print("pair increase")
        #             pairs+=1
        #         else:
        #             print("change came")
        #             came = True
        #             pairs+=1
        #     if came:
        #         prev= maxnum
        #     else:
        #         prev = curr
        # return pairs

        pairs = 0

        index = defaultdict(int)

        for i in range(1,len(nums)):
            prev = nums[i-1]
            curr = nums[i]

            if prev == curr:
                pairs+=1
            else:
                index[(prev,curr)]+=1
                index[(curr,prev)]+=1
        
        return pairs + (max(index.values()) if index else 0)

        