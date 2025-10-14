class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:

        n = len(nums)
        # we only need to go until len(nums) - 2*k
        for a in range(n - 2 * k + 1):
            prev = nums[a]
            count = 1
            ok1 = True
            ok2 = True

            # Check first subarray
            for i in range(a + 1, a + k):
                on = nums[i]
                if on <= prev:   # not strictly increasing
                    ok1 = False
                    break
                prev = on

            # Check second subarray only if first is ok
            if ok1:
                prev = nums[a + k]
                for i in range(a + k + 1, a + 2 * k):
                    on = nums[i]
                    if on <= prev:
                        ok2 = False
                        break
                    prev = on

            if ok1 and ok2:
                return True

        return False


