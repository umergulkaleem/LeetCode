class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # arr = [abs(i) for i in nums]

        # while nums:
        #     arr.append(nums%10)
        #     nums = nums//10
        # print(abs(nums))
        # print(arr)
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],
        nums[-1]*nums[-2]*nums[0],
        nums[-1]*nums[0]*nums[1],
        nums[1]*nums[0]*nums[2]

        )
        