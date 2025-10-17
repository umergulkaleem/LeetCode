class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # all = []
        # for i in range(len(nums)):
        #     temp = []
        #     temp.append(nums[i])
            
        #     for k in range(len(nums)):
        #         if nums[k] not in temp:
        #             temp.append(nums[k])
        #     print(temp)
        #     if temp not in all:
        #         all.append(temp)
        return list(itertools.permutations(nums))

                

        